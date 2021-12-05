from __future__ import division, print_function
import sys
import os
import glob
import re
import numpy as np
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from PIL import Image
from sklearn.preprocessing import OneHotEncoder


encoder = OneHotEncoder()
encoder.fit([[0], [1]]) 

app = Flask(__name__)

model = load_model('models/model_brain.h5')
model1 = load_model('models/pneumo_predict.h5')

def model_predict1(img_path, model):
    test_image = image.load_img(img_path, target_size = (64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = model1.predict(test_image)
    
    if result[0][0] == 1:
        prediction = 'Pneumonia'
        return prediction
    else:
        prediction = 'Normal'
        return prediction


def model_predict(img_path, model):

    img = Image.open(img_path)
    x = np.array(img.resize((128,128)))
    x = x.reshape(1,128,128,3)
    res = model.predict_on_batch(x)

    return res 


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':

        f = request.files['file']
 
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        res = model_predict(file_path, model)

        def names(number):
            if(number == 0):
                return 'a tumor'
            elif(number == 1):
                return 'a no tumor'
        
        classification = np.where(res == np.amax(res))[1][0]
        pred = str(res[0][classification]*100) + '% Confidence This Is ' + names(classification)
        return pred
    return None

@app.route('/predictAnything',methods=['GET','POST'])
def uploadPneumo():
    if request.method == 'POST':

        f = request.files['file']


        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)


        preds = model_predict1(file_path, model1)
        return preds
    return None



if __name__ == '__main__':
    app.run(threaded=True, port=5000)
