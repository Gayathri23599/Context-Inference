import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
def pre_processing(inp):
	porter_stemmer = PorterStemmer()
	wordnet_lemmatizer = WordNetLemmatizer()

#word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
# First Word tokenization
	l = []
	nltk_tokens = nltk.word_tokenize(inp)
	for w in nltk_tokens:
		l.append(porter_stemmer.stem(w))
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
