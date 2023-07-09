from flask import Flask, render_template, request
from utils import get_stopwords_removal, get_lemmatized_stemmed_word
import nltk
from nltk.tokenize import word_tokenize

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
  if request.method == "GET":
    return render_template("index.html")
  
  else:
    lang = request.form['language']
    stem_lemm_type = request.form['stemmer_lemmatizer']
    sentence = request.form['sentence']
    case_folding = sentence.lower()
    tokenize_word = [w for w in word_tokenize(case_folding) if w.isalnum()]
    stopword_removal_word = get_stopwords_removal(tokenize_word, lang)
    stem_lemm_word = get_lemmatized_stemmed_word(stopword_removal_word, stem_lemm_type)
    
  return render_template("index.html", 
                         sentence=sentence, 
                         lang=lang,
                         stem_lemm_type=stem_lemm_type,
                         case_folding=case_folding, 
                         tokenize_word=tokenize_word, 
                         stopword_removal_word=stopword_removal_word, 
                         stem_lemm_word=stem_lemm_word)

# if __name__ == '__main__':
# 	app.run(debug=True)