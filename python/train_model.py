#!/usr/bin/env python3
#Build a small Pixel CNN++ model to train on MNIST.

import tensorflow as tf
import tensorflow_datasets as tfds
import tensorflow_probability as tfp
import numpy as np
from dataset_prep import like_mnist
import pickle
import os
import configparser
import argparse
import os
import re
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers

#limit verbositys
tf.get_logger().setLevel('ERROR')

# import matplotlib.pyplot as plt
#parser = argparse.ArgumentParser()
#parser.add_argument('temprature', type=float, nargs='+',
#                    help='temperature of 0.5 increments')
#parser.add_argument('length', type=int, nargs='+',
#                    help='size of lattice')
#parser.add_argument('checkpoints',type=str, default ='None',
#                    help='this is a path to the directory containing the pretrained weights')
#parser.add_argument('epochs',type=int, default ='None',
#                    help='these are the epochs')
#args = parser.parse_args()

#T = args.temprature[0]
#L = args.length[0]
#cp_path = args.checkpoints
#epochs = args.epochs[0]
#epochs = 2

config = configparser.ConfigParser()
config.read("run.param")
T = float(config['input']['T'])
L = int(config['input']['L'])
epochs = int(config['input']['epochs'])
batch_size = int(config['input']['batch_size']) 
learning_rate = float(config['input']['learning_rate']) 
shuffbuff = int(config['input']['shuffbuff']) 
training_samples = int(config['input']['training_samples']) 
test_samples = int(config['input']['test_samples']) 
heirarchies = int(config['input']['heirarchies']) 
filters = int(config['input']['filters']) 
logistic_mix = int(config['input']['logistic_mix']) 
dropout = float(config['input']['dropout']) 
num_resnet = int(config['input']['num_resnet'])
tfd = tfp.distributions
tfk = tf.keras
tfkl = tf.keras.layers

#Line for dependencies
gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)

# tf.enable_v2_behavior()
results = []

#trying my dataset out
image_shape, data = like_mnist(T,L)
# train_data, test_data = data['train'], data['test']
# print(train_data,test_data)
# data = data.shuffle(shuffbuff)
train_data = data.take(training_samples)
test_data = data.skip(training_samples).take(int(training_samples/10))

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)

def image_preprocess(x):
    #x['image'] = tf.cast(x['image'], tf.float32)
    x['image'] = tf.cast(x['image'], tf.int8)
    return (x['image'],)  # (input, output) of the model

def random_invert_sample(x, p=0.5):
    if  tf.random.uniform([]) < p:
        x = x.map(lambda x: x*-1)
    else:
        x
    return x
      
#def random_invert(factor=0.5):
#    return layers.Lambda(lambda x: random_invert_img(x, factor))

#random_invert = random_invert()


#class RandomInvert(layers.Layer):
#    def __init__(self, factor=0.5, **kwargs):
#        super().__init__(**kwargs)
#        self.factor = factor


#    def call(self, x):
#        return random_invert_img(x)

#create a data augmentaion stage
data_augmentation = keras.Sequential(
    [
        layers.RandomTranslation(
            height_factor = 0.99,
            width_factor = 0.99,
            fill_mode="wrap"
            ),
        #RandomInvert(),
        ]
        )

#train_it = train_data.map(image_preprocess).batch(batch_size).shuffle(shuffbuff).map(data_augmentation)
train = train_data.map(image_preprocess).batch(batch_size).shuffle(shuffbuff).map(data_augmentation)
train_it = layers.Lambda(random_invert_sample)(train)



#train_it = train_data.map(image_preprocess).batch(batch_size).shuffle(shuffbuff)
test_it = test_data.map(image_preprocess).batch(batch_size).shuffle(shuffbuff)


# Define a Pixel CNN network
dist = tfd.PixelCNN(
    image_shape=image_shape,
    num_resnet=num_resnet,
    num_hierarchies=heirarchies,
    num_filters=filters,
    num_logistic_mix=logistic_mix,
    dropout_p=dropout,
    high=1
)

# Define the model input
image_input = tfkl.Input(shape=image_shape)

# Define the log likelihood for the loss fn
log_prob = dist.log_prob(image_input)

#Search and list saved weights
dirs = [s for s in os.listdir() if s.startswith("weights")]
print(dirs, '\n\n\n')
# Define the model
model = tfk.Model(inputs=image_input, outputs=log_prob)
model.add_loss(-tf.reduce_mean(log_prob))
 
# Save weights to  checkpoint file
checkpoint_path = "weights/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

#import useful callback functions 
from keras.callbacks import ModelCheckpoint, EarlyStopping, CSVLogger

# Create a callback object that saves the model's weights
checkpoint = ModelCheckpoint(filepath=checkpoint_path, 
        monitor='val_loss', 
        verbose=1, 
        save_best_only=True, 
        save_weights_only=True, 
        mode='min')

#Stops training if imporvment is no longer being observed
earlystop = EarlyStopping(monitor='val_loss', patience=4, verbose=1)

#CSVLogger logs epoch, acc, loss, val_acc, val_loss
log_csv = CSVLogger('log.csv',separator=',', append=True)

callbacks_list = [checkpoint, earlystop, log_csv]

#Make function to extract int val for epoch weights
#def get_weights(s):
#    m = re.search('weights')
#    return int(m.group(1))

#load available weights marked by saved epoch value
#weights = list(map(get_weights, dirs))

if len(dirs) != 0:
    model.load_weights('weights/cp.ckpt')
    df = pd.read_csv('log.csv')
    initial_epoch = len(df)
    model.compile(
        optimizer=tfk.optimizers.Adam(learning_rate),
        metrics=[])
else:  
    # Compile and train the model
    model.compile(
        optimizer=tfk.optimizers.Adam(learning_rate),
        metrics=[])
    initial_epoch = 0

print("Fitting...")
H = model.fit(train_it,
          epochs=epochs,
          #initial_epoch=initial_epoch,
          initial_epoch=initial_epoch,
          verbose=1,
          validation_data=test_it,
          callbacks=callbacks_list)  # Pass callback to training

    
# save training loss
#loss = np.zeros((2,epochs))
#loss[0,:], loss[1,:] = np.arange(0, epochs), H.history["loss"]
#np.savetxt('loss.dat',np.c_[loss[0,:],loss[1,:]])
#np.savetxt((str(t)+'/loss.dat'),H.history["loss"])

# save val loss
#val_loss = np.zeros((2,epochs))
#val_loss[0,:], val_loss[1,:] = np.arange(0, epochs), H.history["val_loss"]
#np.savetxt(('validation_loss.dat'), np.c_[val_loss[0,:],val_loss[1,:]])

