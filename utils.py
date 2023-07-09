import nltk
from nltk.corpus import stopwords
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

from mpstemmer import MPStemmer
# https://github.com/ariaghora/mpstemmer

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# https://github.com/har07/PySastrawi/tree/master

def get_stopwords_removal(input_words, language_input='indonesia'):
    language = language_input
    language_list_nltk = ['arabic',
    'azerbaijani',
    'danish',
    'dutch',
    'english',
    'finnish',
    'french',
    'german',
    'greek',
    'hungarian',
    'indonesian',
    'italian',
    'kazakh',
    'nepali',
    'norwegian',
    'portuguese',
    'romanian',
    'russian',
    'slovene',
    'spanish',
    'swedish',
    'tajik',
    'turkish']


    if language == 'indonesia':
      sw = StopWordRemoverFactory().get_stop_words()
    elif language in language_list_nltk:
      sw = stopwords.words(language_input)
    else:
      sw = []

    clean_word = [w for w in input_words if w not in sw]

    return clean_word

def get_lemmatized_stemmed_word(input_words, lemmatizer_stemmer='mp'):
  result = None
  if lemmatizer_stemmer == 'porter':
    porter_stemmer_obj = PorterStemmer()
    result = [porter_stemmer_obj.stem(w) for w in input_words]
  elif lemmatizer_stemmer == 'wordnet':
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmatize_result_V = [wordnet_lemmatizer.lemmatize(w, pos='v') for w in input_words]
    result = [wordnet_lemmatizer.lemmatize(w, pos='n') for w in lemmatize_result_V]
  elif lemmatizer_stemmer == 'mp':
    mp_stemmer = MPStemmer()
    result = [mp_stemmer.stem(w) for w in input_words]
  else:
    factory = StemmerFactory()
    sastrawi_stemmer = factory.create_stemmer()
    result = [sastrawi_stemmer.stem(w) for w in input_words]

  return result