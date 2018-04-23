import emot
import operator
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
import matplotlib.backends.backend_pdf

skin_tones = set(['🏻', '🏼', '🏽', '🏾', '🏾'])

def count_emojis(text):
	global skin_tones

	text = text.replace(':', '')
	emojis_counter = {}
	emojis = emot.emoji(text)
	for map_emoji in emojis:
		try:
			if(map_emoji['value'] not in skin_tones):
				emojis_counter[map_emoji['value']] += 1
		except KeyError as e:
			if(map_emoji['value'] not in skin_tones):
				emojis_counter[map_emoji['value']] = 1
	emojis_counter_sorted = sorted(emojis_counter.items(), key=operator.itemgetter(1), reverse=True)
	return emojis_counter_sorted


def main():
	fp = open('./emojis/cloudwordsEmojis-eleicoes.txt', 'r')
	counter = count_emojis(fp.read())
	labels = [ec for ec in range(len(counter[:5]))]
	values = [ec[1] for ec in counter[:5]]
	print(values)
	print([ec[0].encode('unicode-escape') for ec in counter[:5]])
	plt.bar(labels, values)
	plt.show()

if __name__ == '__main__':
	main()


