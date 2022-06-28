from bs4 import BeautifulSoup
import string
import spacy
from nltk.tokenize import word_tokenize

import nltk
try:
    #check if nltk download is available
    pass
except:
    #nltk.download('punkt')
    pass

sp = spacy.load('en_core_web_sm')
all_stopwords = sp.Defaults.stop_words

class Preprocess:
    def __init__(self):
        pass
        
    #Creating a function to remove unicode characters
    def clean(self, text):
        text= text.replace("\xa0","")
        text= text.replace("\x95","")
        text= text.strip()
        return str(text)
    
    #Creating a function to remove HTML tags
    def remove_html(self, text):
        soup= BeautifulSoup(text,'lxml')
        text= soup.get_text()
        return str(text)
    
    #Creating funciton to remove punctuation
    def remove_punctuations(self, text):
        for punctuation in string.punctuation:
            text = text.replace(punctuation, '')
            return str(text)
        
    #Creating a function to remove stopwords
    def remove_stopwords(self, text):
        text_tokens = word_tokenize(text)
        tokens_without_sw= [word for word in text_tokens if not word in all_stopwords]
        text = (" ").join(tokens_without_sw)
        return str(text)
    
    #Creating a function to remove Digits
    def remove_digits(self, text):
        text = ''.join(c for c in text if not c.isdigit())
        return str(text)
    
    #Creating a Pipeline to call all functions
    def pipeline(self, text):
        text = self.clean(text)
        text = self.remove_html(text)
        text = self.remove_punctuations(text)
        text = self.remove_stopwords(text)
        text = self.remove_digits(text)
        return text
  