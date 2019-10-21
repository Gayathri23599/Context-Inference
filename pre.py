import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
def pre_processing(inp):
	porter_stemmer = PorterStemmer()
	stop_words = set(stopwords.words('english'))
	wordnet_lemmatizer = WordNetLemmatizer()

#word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
# First Word tokenization
	l = []
	nltk_tokens = nltk.word_tokenize(inp)
	l = [w for w in nltk_tokens if not w in stop_words]
	#for w in nltk_tokens:
	#	l.append(porter_stemmer.stem(w))
		#l.append(wordnet_lemmatizer.lemmatize(w))
	return l
#Next find the roots of the word
#for w in nltk_tokens:
#      print "Actual: %s  Stem: %s"  % (w,porter_stemmer.stem(w))
#import nltk



#word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
#nltk_tokens = nltk.word_tokenize(word_data)
#for w in nltk_tokens:
#       print "Actual: %s  Lemma: %s"  % (w,wordnet_lemmatizer.lemmatize(w))
