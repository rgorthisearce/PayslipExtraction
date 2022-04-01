import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import spacy

import pytesseract
import pdfplumber

app = Flask(__name__)
model = pickle.load(open('finalized_model.sav', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    file = [int(x) for x in request.form.values()]
    
    if (isPDF):
        with pdfplumber.open(file) as pdf:
            first_page = pdf.pages[0]
            text = first_page.extract_text()
            
    else:
        text = pytesseract.image_to_string(file)
    
    nlp_doc = model(text)
    
    output = spacy.displacy.render(result, style="ent")

    return render_template('index.html', prediction_text='Entities in the text are: $ {}'.format(output))

