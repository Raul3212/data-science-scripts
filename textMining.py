#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import re
from nltk.tokenize import TweetTokenizer
import nltk
from emoji.unicode_codes import UNICODE_EMOJI
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

# def tree_tagger(palavras):
#     palavras_str = ' '.join(palavras)
#     ps = subprocess.Popen(['echo', '"{}"'.format(palavras_str)], stdout=subprocess.PIPE)
#     output = subprocess.check_output(('/home/romulo/PUC/2018.1/DataScience/TreeTagger/cmd/tree-tagger-portuguese'), stdin=ps.stdout)
#     print (output)
#     result = []
#     result_por_palavra = str(output).split('\\n')[1:-2]
#     print(result_por_palavra)
#     for r in result_por_palavra:
#         l = r.split('\\t')
#         if l[2] == '<unknown>':
#             l[2] = l[0]
#         result.append(tuple(l)[1:])
#     return result

def preProcessing(twitterText):

	#Remover \n
	twitterText = re.sub("\n+"," ",twitterText)

	#Remover multiplos espaços
	twitterText = re.sub(" +"," ",twitterText)

	#Remove links
	twitterText = re.sub(r"http\S+", "",twitterText)

	#Remover caracteres especiais
	twitterText = re.sub("[@|#|“|”|’|‘|®|,|!|?||\[|\]|\.|\"|%|:|\-|_|/|ª|\(|\)|°|\*|🇧|🇷|\'|️|=]",'',twitterText)

	#Remover números
	twitterText = re.sub("[0-9]+",'',twitterText)

	#Lower case
	twitterText = twitterText.lower()

	#Tokenize
	twitterTokens = TweetTokenizer().tokenize(twitterText)

	#remove stopwords
	stopwords = nltk.corpus.stopwords.words('portuguese')
	stopwords.remove("não")
	stopwords.remove("num")
	twitterTokens = [token for token in twitterTokens if (token not in stopwords) ]

	return ' '.joint(twitterTokens)

def generateCloudWords(dirFileTwitter,nameCandidate):
	#criar arquivo
	dirfileSave = "DATASETCLEAN/cloudwordsEmojis-"+nameCandidate+".txt"
	dirImgSave = "cloudwords/cloudwordsEmojis-"+nameCandidate+".png"
	generateFileFromTwitter(dirFileTwitter,dirfileSave)

	#criar nuvem de palavras
	dir = path.dirname(__file__)
	text = open(path.join(dir, dirfileSave)).read()
	mask = np.array(Image.open(path.join(dir,"twitter_mask.png" )))
	cloud = WordCloud(background_color='white', max_words=2000, mask=mask)
	cloud.generate(text)
	cloud.to_file(dirImgSave)

def onlyFilesInDir(directory):
	return [f for f in listdir(directory) if isfile(join(directory, f))]

def generateFileFromTwitter(dirFileTwitter):
	with open(dirFileTwitter) as f:
    for line in f:
        <do something with line>
	
		
if __name__ == "__main__":

	#listRun = [("DATASET/TEMER","temer"),("DATASET/LULA","lula"),("DATASET/GILMAR","gilmar"),("DATASET/BOLSONARO","bolsonaro"),("DATASET/ALVARO","alvaro"),("DATASET/ALCKMIN","geraldoAlckmin"),("DATASET/MARINA","marinaSilva"), ("DATASET/CIRO","ciroGomes") , ("DATASET/MAIA","rodrigoMaia") ]
	listRun = [ ("DATASET/MANUELA","manuela") ,("DATASET/ELEICOES","eleicoes") ]
	for dirDataset,name in listRun:
		print(">>>> ",name)
		generateCloudWords(dirDataset,name)
