from bs4 import BeautifulSoup
import string
import spacy
from nltk.tokenize import word_tokenize

import nltk
nltk.download('punkt')

sp = spacy.load('en_core_web_sm')
all_stopwords = sp.Defaults.stop_words

class Preprocess:
    def __init__(self, text):
        self.pipeline(text)
    def clean(self, text):
        text= text.replace("\xa0","")
        text= text.replace("\x95","")
        return str(text)
    def remove_html(self, text):
        soup= BeautifulSoup(text,'lxml')
        text= soup.get_text()
        return str(text)
    def remove_punctuations(self, text):
        for punctuation in string.punctuation:
            text = text.replace(punctuation, '')
            return str(text)
    def remove_digits(self, text):
        text = ''.join(c for c in text if not c.isdigit())
        return str(text)
    def pipeline(self, text):
        text = self.clean(text)
        text = self.remove_html(text)
        text = self.remove_punctuations(text)
        text = self.remove_stopwords(text)
        text = self.remove_digits(text)
        return text
  