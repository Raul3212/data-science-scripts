import re
from nltk.tokenize import TweetTokenizer
import nltk

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