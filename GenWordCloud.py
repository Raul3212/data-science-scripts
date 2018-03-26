import wordcloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import optparse
from wordcloud import WordCloud
from os import path

def main():
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file', dest='fileName')
    parser.add_option('-i', '--image', dest='imageMask')
    parser.add_option('-o', '--output', dest='outputFile')

    (options, args) = parser.parse_args()

    dir = path.dirname(__file__)
    text = open(path.join(dir, options.fileName)).read()
    mask = np.array(Image.open(path.join(dir, options.imageMask)))
    cloud = WordCloud(background_color='white', max_words=2000, mask=mask)
    cloud.generate(text)
    cloud.to_file(options.outputFile)
    print('Arquivo salvo em \'{}\'. Tchau!'.format(options.outputFile))

if __name__ == '__main__':
    main()