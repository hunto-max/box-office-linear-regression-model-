
# A very simple for you to get started with...

from flask import Flask, request , render_template
import pickle
import pandas as pd

app = Flask(__name__)

#loading pickle file
box_office_prediction_model= pickle.load(open('/home/m3456/mysite/box_office_prediction_model.pkl', 'rb'))

#route for homepage
@app.route('/')
def index():
    return '<h1>Homepage</h1>'

#route for campagin classification model 1
@app.route('/classification')
def classification():
    return "<h1>Marketing Campaign Classification Model</h1>"

#route for regression model
@app.route('/regression')
def box_office_prediction():
    return render_template('box_office_prediction.html')

#route for image classification model
@app.route('/image classification')
def box_office():
    return "<h1>Image classification Model</h1>"
