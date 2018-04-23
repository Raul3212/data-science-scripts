import json
import re
from nltk.tokenize import TweetTokenizer
import nltk
import emoji
import subprocess
from os import listdir
from os.path import isfile, join
import wordcloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import optparse
from wordcloud import WordCloud
from os import path
import pandas as pd

sentiLex = {}
emojiSentiment = {}

def loadSentiLexAndEmojiSentiment():
	global emojiSentiment,emojiSentiment
	
	#SentiLex
	sentiLexFile = open("./SentiLex-PT01/SentiLex-flex-PT01.txt","r")
	lines = sentiLexFile.readlines()
	for line in lines:
		splitedLine = line.split(".")
		
		words = splitedLine[0]
		words = words.split(',')

		score = splitedLine[1].split(';')
		score = int(score[3].split('=')[1])
		
		for word in words:
			sentiLex[word] = score

	#Emoji Sentiments
	df = pd.read_csv('./Emoji Sentiment Ranking v1.0.csv')
	emojiSentiment = dict(zip(df['Char'], df['SentimentScore']))
	
def termScoreSummationMethod(twitterText):
	global emojiSentiment,emojiSentiment

	score = 0
	twitterTextTokens = TweetTokenizer().tokenize(twitterText)

	for token in twitterTextTokens:
		if(token in emojiSentiment):
			score+=emojiSentiment[token]
		if(token in sentiLex):
			score+= sentiLex[token]

	if(score< 0):
		return -1
	if(score >0):
		return 1
	else:
		return 0

def runClassification(dirFileTwitter):
	with open(dirFileTwitter) as f:
		for line in f:
			termScoreSummationMethod(line)
