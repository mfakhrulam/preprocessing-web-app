import nltk
from nltk.corpus import stopwords
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer

from mpstemmer import MPStemmer
# https://github.com/ariaghora/mpstemmer

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# https://github.com/har07/PySastrawi/tree/master

def get_stopwords_removal(input_words, language_input='indonesia'):
    language = language_input
    language_list_nltk = ['arabic','azerbaijani','danish','dutch','english','finnish','french','german','greek','hungarian','indonesian','italian','kazakh','nepali','norwegian','portuguese','romanian','russian','slovene','spanish','swedish','tajik','turkish']
    if language == 'indonesia':
      sw = StopWordRemoverFactory().get_stop_words()
    elif language in language_list_nltk:
      sw = stopwords.words(language_input)
    else:
      sw = []

    clean_word = [w for w in input_words if w not in sw]

    return clean_word

def get_lemmatized_stemmed_word(input_words, lemmatizer_stemmer='mp'):
  result = {}
  if lemmatizer_stemmer == 'porter':
    porter_stemmer_obj = PorterStemmer()
    result['output_words'] = [porter_stemmer_obj.stem(w) for w in input_words]
    result['desc'] = 'Porter Stemmer adalah algoritma stemming yang dikembangkan oleh Martin Porter pada tahun 1979. Tujuannya adalah memangkas akhiran kata dalam bahasa Inggris untuk menghasilkan bentuk dasar yang lebih umum. Algoritma ini mengikuti serangkaian aturan dan langkah-langkah pemangkasan berdasarkan struktur morfologis kata dalam bahasa Inggris. Dalam pemrosesan, akhiran seperti "-s", "-ed", "-ing" dihapus, dan kata-kata diubah sesuai dengan aturan yang ditentukan.'
  elif lemmatizer_stemmer == 'wordnet':
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmatize_result_V = [wordnet_lemmatizer.lemmatize(w, pos='v') for w in input_words]
    result['output_words'] = [wordnet_lemmatizer.lemmatize(w, pos='n') for w in lemmatize_result_V]
    result['desc'] = 'WordNet Lemmatizer adalah sebuah algoritma dalam pemrosesan bahasa alami yang menggunakan WordNet, sebuah kamus bahasa Inggris, untuk mengubah kata-kata dalam teks menjadi bentuk dasar atau kata dasar yang lebih umum. Teknik ini melibatkan mencocokkan kata-kata dengan entri-entri dalam WordNet dan menerjemahkan kata-kata ke bentuk dasar yang sesuai berdasarkan relasi semantik dan leksikal'
  elif lemmatizer_stemmer == 'mp':
    mp_stemmer = MPStemmer()
    result['output_words'] = [mp_stemmer.stem(w) for w in input_words]
    result['desc'] = 'Multi-phase Stemmer adalah algoritma pemangkasan kata yang khusus dirancang untuk bahasa Indonesia. Algoritma ini didasarkan pada penelitian Adriani et al. (2007) dan telah dimodifikasi agar dapat bekerja dengan kata-kata standar (baku) dan nonstandar (tak baku) yang umum digunakan dalam bahasa Indonesia.'
  elif lemmatizer_stemmer == 'lancaster':
    lc_stemmer = LancasterStemmer()
    result['output_words'] = [lc_stemmer.stem(w) for w in input_words]
    result['desc'] = 'Lancaster Stemmer adalah algoritma stemming yang digunakan untuk memotong akhiran kata secara agresif dengan menggunakan aturan pemotongan berbasis heuristik. Lancaster Stemmer menghapus prefiks dan akhiran kata secara radikal untuk mencapai bentuk dasar yang lebih singkat. Meskipun algoritma ini dapat memangkas kata-kata secara agresif, kekurangannya adalah kemungkinan menghasilkan kata dasar yang tidak valid atau tidak terkait dengan kata aslinya.'
  elif lemmatizer_stemmer == 'snowball':
    sb_stemmer = SnowballStemmer('english')
    result['output_words'] = [sb_stemmer.stem(w) for w in input_words]
    result['desc'] = 'Snowball Stemmer, juga dikenal sebagai Porter2 Stemmer, adalah sebuah algoritma stemming yang dirancang untuk memotong akhiran kata dalam berbagai bahasa. Algoritma ini dikembangkan oleh Martin Porter sebagai perbaikan dari algoritma stemming sebelumnya, yaitu Porter Stemmer.'
  else:
    factory = StemmerFactory()
    sastrawi_stemmer = factory.create_stemmer()
    result['output_words'] = [sastrawi_stemmer.stem(w) for w in input_words]
    result['desc'] = 'Sastrawi Stemmer adalah algoritma stemming yang dikembangkan untuk bahasa Indonesia. Algoritma ini menggunakan aturan-aturan pemotongan berbasis heuristik yang dirancang khusus untuk memangkas akhiran kata dalam bahasa Indonesia dan menghasilkan bentuk dasar yang lebih umum.'

  return result