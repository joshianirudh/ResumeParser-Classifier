from tensorflow import keras
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences


class Model:
    def __init__(self):
        pass
        #self.normalize(text) 
    #Creating a function to run the model and classify the resume text
    def predict_out(self, text):
        model = keras.models.load_model('/Users/abhaylal/Desktop/DeepLearning/ResumeParser-Recommender/Notebooks/model_weights/conv.h5')
        pred = model.predict(text)
        return pred
    #Creating a function to return a list of outputs based on the proabilities of each class
    def format(self, text):
        tokenizer = Tokenizer(num_words=1000, lower=True)
        tokenizer.fit_on_texts(text)
        sequences = tokenizer.texts_to_sequences(text)
        x = pad_sequences(sequences, maxlen=256)
        return x
    def normalize(self, text):
        print("*********",len(text))
        pred = self.predict_out(self.format(text))
        list_out = []
        print("*********",type(pred[0]),pred.shape, type(pred[0]), pred[0].shape)
        for j in pred[0]:
            if j>=0.25:
                list_out.append(1)
            else:
                list_out.append(0)
        return list_out
        
    
        
          