import numpy as np
import pandas as pd

#vowel count: ['a','e','i','u','o']
#y count: ['y']

def date_time_md(df):
    days = []
    date = []
    time = []
    year = []
#    df = pd.readcsv(filename)
    for i in range(len(df)):
        string = df['created_at'][i]
        t_stamp = string.split()
        days.append(t_stamp[0])
        date.append(t_stamp[1]+' '+t_stamp[2])
        time.append(t_stamp[3])
        year.append(t_stamp[5])

    df['Day']=days
    df['Date']=date
    df['Time']=time
    df['Year']=year

    df = df.drop('created_at',axis=1)
    df = df.drop('lang',axis=1)


    return df

def poem_text_md(df):
    poems = []
    word_count = []
    hashtags = []
    hashtag_count = []
    chars = []
    vowel_tally = []
    y_tally = []
    vowels = ['u','o','i','a','e']
    y = 'y'
    for i in range(len(df)):
        poem = []

        hashtag = []

        character_count = 0

        v_count = 0

        y_count = 0

        spot = df['full_text'][i]

        words = spot.split()
        for word in words:
            if not word.find('#'):
                hashtag.append(word)
            else:
                character_count += len(word)
                poem.append(word + " ")
                for vowel in vowels:
                    v_count += word.count(vowel)
                y_count += word.count(y)
        chars.append(character_count)
        word_count.append(len(poem))
        poems.append("".join(poem))
        hashtags.append(hashtag)
        hashtag_count.append(len(hashtag))
        y_tally.append(y_count)
        vowel_tally.append(v_count)

    df['character_count']=chars
    df['word_count']=word_count
    df['hashtags']=hashtags
    df['poems']=poems
    df['hashtag_count']=hashtag_count
    df['y_tally']=y_tally
    df['vowel_tally']=vowel_tally
    return df

def twitter_link(df):
    hyperlinks = []
    for id in df['id']:
        hyperlinks.append('twitter.com/anyuser/status/'+str(id))
    df['hyperlinks']=hyperlinks

    return df
