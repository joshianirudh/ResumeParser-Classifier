#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:02:50 2022

@author: nat
"""

from typing import final
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from Scripts.Preprocess import Preprocess
from Scripts.Model import Model

pre_process = Preprocess()
app = Flask(__name__)

app.config['UPLOAD_EXTENSIONS'] = ['.pdf']
app.config['UPLOAD_PATH'] = 'uploaded_files'

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about/')
def about():
    return render_template('about.html')
@app.route('/layout/')
def layout():
    return render_template('layout.html')

    
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = f.filename
        if filename != '':
          file_ext = os.path.splitext(filename)[1]
          if file_ext not in app.config['UPLOAD_EXTENSIONS']:
              return "Error File not correct format"
     
        f.save(os.path.join(app.config['UPLOAD_PATH'], 'resume.pdf'))
  
        output_string = StringIO()
        with open('uploaded_files/resume.pdf', 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
        STORE = output_string.getvalue()
        if not STORE: 
            return "Error Empty File" 
            quit()  
        
        main_model = Model()
        print(STORE)    
        text = pre_process.pipeline(text=STORE)
        print(main_model.normalize(text))


        OUT = main_model.normalize(text)
        classes = ['Software_Developer', 'Database_Administrator',
           'Systems_Administrator', 'Project_manager',
           'Web_Developer', 'Network_Administrator',
           'Security_Analyst', 'Python_Developer',
           'Java_Developer', 'Front_End_Developer']

        final = []
        for i in range(10):
            if(OUT[i]==1):
                print(classes[i])
                final.append(classes[i])
                
        #s=''.join(final)

        
        textFile = open("uploaded_files/resume.txt", 'a')
        textFile.write(output_string.getvalue())
        textFile.close()
        # Add your function for dealing with the model and get the output and render it on output.html
        return render_template('output.html', variable=final)
        

if __name__ == '__main__':
   app.run(debug = True)
