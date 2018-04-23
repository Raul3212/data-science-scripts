import pandas as pd
import glob
from ClassByEmoji import *
from textMining import *

def main():
	candidato = ''
	jsonFileNames = glob.glob('./*.json')
	file_out = open('{}.csv'.format(candidato), 'w+')
	file_out.write('id,screen_name,name,user_location,full_text,emot_class,semantic_class')
	for jsonFileName in jsonFileNames:
		tweet = pd.read_json(jsonFileName)
		if tweet['lag'] == 'pt':
			simple_tweet = {}
			simple_tweet['id'] = tweet['id']
			simple_tweet['user_location'] = tweet['user']['location']
			simple_tweet['source'] = tweet['source']
			simple_tweet['screen_name'] = tweet['screen_name']
			simple_tweet['name'] = tweet['name']
			text_aux = ''
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
				text_aux = tweet['text']

			simple_tweet['full_text'] = text_aux
			simple_tweet['emot_class'] = classByEmoji(simple_tweet['full_text'])
			simple_tweet['semantic_class'] = termScoreSummationMethod(preProcessing(simple_tweet['full_text']))
			#fazer algo com o tweet
			file_out.write('{},{},{},{},{},{},{}'.format( //
				simple_tweet['id'], //
				simple_tweet['screen_name'], //
				simple_tweet['name'], //
				simple_tweet['user_location'], //
				simple_tweet['full_text'], //
				simple_tweet['emot_class'], //
				simple_tweet['semantic_class'] //
			))
	file_out.close()

if __name__ == '__main__':
	main()