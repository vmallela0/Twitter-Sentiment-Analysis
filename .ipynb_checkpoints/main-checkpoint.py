import nltk # nlp processing toolkit
from textblob import TextBlob, Word, Blobber # hooking up to nltk
import tweepy # for twitter api
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk


# testing nlp polarity/subjectivity
# arg = input("enter a tweet::   ")
# sentimentTest = TextBlob(arg)
# print(format(sentimentTest.sentiment))

consumer_key = 'bUe0HnRooyKBZpzo6de0ZDf4P'
consumer_secret = 'Fx4bgDYsIwVpONwQqJZsuC4kBbc3Ib8TJywLmbJkoTcZdMepmo'
access_token = '1272931080790773763-QYMGjdbWB0COeA8SZFzJxRyHeep9F8'
access_token_secret = 'RCl9BXm4Uz410MOMHT0zcAm5dYit6GgWcvfWaSIITj0fD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def twSearch(search):
    polarity = []
    subjectivity = []
    tweetArr = []

    query = search
    public_tweets = tweepy.Cursor(api.search, q=query, rpp=100, count=200, result_type="recent", include_entities=True, lang="en").items(5) # set to 200
    
    #TODO Possibly also filter other params ex. lang/geo ==> feed into tkinter gui and plot the graph through seaborn/matplot?
    for i in public_tweets:
        tweetArr.append(i.text)
        analysis = TextBlob(i.text)
        polar = analysis.sentiment
        polarity.append(float(polar.polarity))
        subject = analysis.sentiment
        subjectivity.append(float(subject.subjectivity))
        
    twAnalysis = ("polarity::  \n" + str(polarity) + "\n\nsubjectivity::  \n" + str(subjectivity) + "\n\n" + str(tweetArr)) #TODO stop overflow on tweets. 
    tweets = tk.Label(root, text = twAnalysis)
    canvas1.create_window(200,500,window=tweets)
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 600, height = 800)
canvas1.pack()
entry1 = tk.Entry (root) 
entry1.insert(0, "Stanford")

canvas1.create_window(200, 400, window=entry1)

def query():  
    uData = entry1.get()
    twSearch(uData)
    
button1 = tk.Button(text='Query', command=query)
canvas1.create_window(200, 430, window=button1)

root.mainloop()    