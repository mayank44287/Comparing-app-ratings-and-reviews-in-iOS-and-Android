#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:09:13 2020

@author: mayankraj
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

finalList = []
def sentiment_analyzer_scores(sentence, appid, rating,category):
    score = analyzer.polarity_scores(sentence)
    #print("{:-<40} {}".format(sentence, str(score)))
    #del score['compound']
    
#=============================================================================
    if score['compound'] >= 0.05:
        sentiment = 'positive'
    elif score['compound'] <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
#=============================================================================
    
    #finalList.append((appid,sentence,str(max(score.items(), key=operator.itemgetter(1))[0])))
    finalList.append((appid,category,rating,sentence,str(sentiment)))

csv = pd.read_csv("src/data/ios.csv");

df = csv.reset_index()

d1 =  df.drop(columns = ['url','userName','title','userUrl','version'])


#final_df = pd.DataFrame(columns=['review','sentiment'])
analyzer = SentimentIntensityAnalyzer()

for index, row in d1.iterrows(): 
    sentiment_analyzer_scores(row['text'],row['appid'],row['score'], row['category'])
    
    
final_df = pd.DataFrame(finalList)
final_df.columns = ['appid','category','rating','review','sentiment']

final_df.to_csv('src/data/iOSReviewSentimentSingle.csv', sep='\t')



#android analysis
android_csv = pd.read_csv("src/data/android_data.csv");

df1 = android_csv.reset_index()


d2 = df1.iloc[:,1:6]
d2 = d2.drop(columns = ['thumbsUpCount'])

finalList1 = []

def sentiment_analyzer_scores1(sentence, appid, rating, category):
    score = analyzer.polarity_scores(sentence)
    #print("{:-<40} {}".format(sentence, str(score)))
    #del score['compound']
    
    #finalList.append((appid,sentence,str(max(score.items(), key=operator.itemgetter(1))[0])))
#=============================================================================
    if score['compound'] >= 0.05:
        sentiment = 'positive'
    elif score['compound'] <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
#=============================================================================
    #finalList1.append((appid,rating,sentence,str(score)))
    finalList1.append((appid,category,rating,sentence,sentiment))

for index, row in d2.iterrows(): 
    sentiment_analyzer_scores1(row['content'],row['appId'],row['score'], row['category'])
    
final_df1 = pd.DataFrame(finalList1)
final_df1.columns = ['appid','category','rating','review','sentiment']

final_df1.to_csv('src/data/androidReviewSentimentSingle.csv', sep='\t')



# =============================================================================
# fig, ax = plt.subplots(figsize=(15,7))
# final_df1.groupby(['rating','sentiment']).count()['rating'].unstack().plot(ax=ax)
# 
# 
# positive = (final_df1[(final_df1.sentiment=='positive')].rating.values)
# 
# negative = (final_df1[(final_df1.sentiment=='negative')].rating.values)
# 
# neutral = (final_df1[(final_df1.sentiment=='neutral')].rating.values)
# 
# plt.plot(positive)
# plt.show()
# =============================================================================
