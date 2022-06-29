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
## Workflow
![Workflow Image](https://github.com/joshianirudh/ResumeParser-Classifier/blob/main/Images/Workflow.jpeg)

## PreProcessing Pipeline
![Pipeline Image](https://github.com/joshianirudh/ResumeParser-Classifier/blob/main/Images/pipeline.png)

## Model
### Deep Neural Network
![DNN Image](https://github.com/joshianirudh/ResumeParser-Classifier/blob/main/Images/dnn.png)
### Convolutional Neural Network
![CNN Image](https://github.com/joshianirudh/ResumeParser-Classifier/blob/main/Images/cnn.png)

### BERT Classifier
![BERT Image](https://github.com/joshianirudh/ResumeParser-Classifier/blob/main/Images/bert.png)

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
* To install Flask and other dependencies, use the given pip command.
```bash
pip install -r requirements.txt
```
* Running Flask scripts is incredibly easy. All you need to do is enter the following line in your terminal.Open the WEB-APP directory in terminal and write the following commands

```bash
export FLASK_APP=app
flask run
```
## :technologist: Project Created & Maintained By -
![Tech Image](https://github.com/joshianirudh/ResumeParser-Classifier/blob/main/Images/team.png)


## License
Distributed under the MIT License. See `LICENSE` for more information.
