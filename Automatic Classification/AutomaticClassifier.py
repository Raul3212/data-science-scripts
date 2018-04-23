import json
import glob
from ClassByEmoji import *
from PreProcessing import *
from SemanticsClassification import *

def main(candidato,jsonFileNames):
	file_out = open('{}.csv'.format(candidato), 'w+')
	file_out.write('id;user_screen_name;user_name;user_location;full_text;emot_class;semantic_class')
	for jsonFileName in jsonFileNames:
		print("Opening file '{}'".format(jsonFileName))
		tweet = json.load(open(jsonFileName))
		if tweet['lang'] == 'pt':
			simple_tweet = {}
			simple_tweet['id'] = tweet['id_str']
			simple_tweet['user_location'] = tweet['user']['location']
			simple_tweet['source'] = tweet['source']
			simple_tweet['user_screen_name'] = tweet['user']['screen_name']
			simple_tweet['user_name'] = tweet['user']['name']
			text_aux = ''
			if 'is_quoted_status' in tweet:
				if tweet['is_quoted_status'] == 'true':
					if 'extended_tweet' in tweet['quoted_status']:
						text_aux = tweet['text'] + tweet['quoted_status']['extended_tweet']['full_text']
					else:
						text_aux = tweet['text'] + tweet['quoted_status']['text']
			elif 'retweeted_status' in tweet:
				if 'extended_tweet' in tweet['retweeted_status']:
					text_aux = tweet['retweeted_status']['extended_tweet']['full_text']
				else:
					text_aux = tweet['retweeted_status']['text']
			else:
				if 'extended_tweet' in tweet:
					text_aux = tweet['extended_tweet']['full_text']
				else:
					text_aux = tweet['text']

			simple_tweet['full_text'] = text_aux.replace(';','').replace('\n', ' ')
			simple_tweet['emot_class'] = classByEmoji(simple_tweet['full_text'])
			simple_tweet['semantic_class'] = termScoreSummationMethod(preProcessing(simple_tweet['full_text']))
			#fazer algo com o tweet
			file_out.write('"{}";"{}";"{}";"{}";"{}";"{}";"{}"\n'.format( simple_tweet['id'], simple_tweet['user_screen_name'], simple_tweet['user_name'], simple_tweet['user_location'], simple_tweet['full_text'],simple_tweet['emot_class'], simple_tweet['semantic_class']))
	file_out.close()

if __name__ == '__main__':
	candidato = 'ALVARO'
	jsonFileNames = glob.glob('/home/romulo/PUC/2018.1/DataScience/ProjetoFinal/DATASET/{}/*.json'.format(candidato))
	loadSentiLexAndEmojiSentiment()
	main(candidato,jsonFileNames)