# ResumeParser-Classifier system
## About Project:
This project is broadly divided into two sections: the Resume Parser and then the Classifier .This project is aimed at building a multi-label classification model using the principles of Deep Learning and NLP to effectively classify users into job categories given their resume.
For the Resume Parser, the raw text will be extracted from resumes and blocks would be isolated along with the separation of entities. 
The model classifies an input resume into categories of IT jobs, a resume can belong to multiple categories.Since this is a multi-label classification problem we will pre-process the text using NER(Name Entity recognition) and use different model architectures like DNN,CNN,LSTM and Bert CLassifier to predict the final class. 

## Business Use case:
*   Our deep learning project can be used by users to find the job description as per their resume.
*   What kind of job might be the most appropriate and where the seekeers could find them is the base problem we are trying to solve. 
*   It can be used by companies with heavy work-loads to pass the candidate resumes through our application to check what all IT roles a certain resume fits into.
*   Creates an executive or management summary that recruiters may use to evaluate candidates by reading. It enables you to quickly arrange the resumes of the candidates. 
*   It takes less time to assess and pick the most relevant talent who is a good fit for your business.

## PreProcessing Pipeline
![Pipeline Image](https://github.com/joshianirudh/ResumeParser-Classifier/blob/main/Images/pipeline.png)

## Model
### Deep Neural Network
![DNN Image](https://github.com/joshianirudh/ResumeParser-Classifier/blob/main/Images/dnn.png)
![CNN Image](https://github.com/joshianirudh/ResumeParser-Classifier/blob/main/Images/cnn.png)

## TechStack Used(Python Libraries):
* BeautifulSoup4
* Flask
* Keras_Preprocessing
* Nltk
* Pandas
* Pdfminer
* Spacy
* Tensorflow
* Werkzeug

## Instructions to run


## Prerequisites 

## :technologist: Project Created & Maintained By -



## License
Distributed under the MIT License. See `LICENSE` for more information.
