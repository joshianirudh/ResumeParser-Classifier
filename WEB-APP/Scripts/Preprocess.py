from bs4 import BeautifulSoup
import string
import spacy
from nltk.tokenize import word_tokenize
import re

import nltk
try:
    #check if nltk download is available
    pass
except:
    #nltk.download('punkt')
    pass
nlp = spacy.load('en_core_web_sm')
sp = spacy.load('en_core_web_sm')
all_stopwords = sp.Defaults.stop_words
remove_ents = ["DATE", "CARDINAL", "GPE", "ORDINAL", "PERCENT", "TIME"]

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
    
    def NER(self, text):
        ents = [ent for ent in nlp(text).ents]
        return str(ents)
    def remove_unwanted_tags(self, text):
        x_spc= nlp(text)
        x_return= ''
        idx= 0
        idx_last_ent= 0
        len_last_ent= 0

        for i, ent in enumerate(x_spc.ents):
            idx= text.find(ent.text)
            if i == 0:
                x_return= text[0: idx]
            else:
                x_return= x_return + text[idx_last_ent+ len_last_ent: idx]

            if ent.label_ not in remove_ents:
                x_return= x_return+ ent.text

            if i== len(x_spc.ents)-1:
                x_return= x_return+ text[idx+len(ent.text): ]

            len_last_ent= len(ent.text)
            idx_last_ent= idx

        x_return= x_return.lower()

        x_return= re.sub('[^\sa-z]', '', x_return)

        x_return= ' '.join([x for x in x_return.split(' ') if (len(x)> 1)])

        #displacy.render(x_spc, style= 'ent', jupyter= True)

        return x_return
    
    #Creating a Pipeline to call all functions
    def pipeline(self, text):
        text = self.clean(text)
        text = self.remove_html(text)
        text = self.remove_punctuations(text)
        text = self.remove_stopwords(text)
        text = self.remove_digits(text)
        text = self.NER(text)
        text = self.remove_unwanted_tags(text)  
        return text
  