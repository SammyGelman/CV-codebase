import os
import pandas as pd

num_poems = 17
df = pd.read_csv("shuffled_poems.csv")

for i in range(num_poems):
    poem = df["poems"][700+i]
    action = os.system('mkdir %s' % (str(700+i)))
    action2 = os.system('python /home/sami_bb/VQGAN-CLIP/generate.py -p "%s" -s 575 575 -se 25 -i 575' % (str(poem)))
    action3 = os.system('mv output.png %s' % (str(700+i)))
    with open('poem.txt', 'w') as f:
            f.write(poem)
    action4 = os.system('mv poem.txt %s' % (str(700+i)))

