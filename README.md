# brain_tumor_detection
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is simple web app for tumor detection.
	
## Technologies
Project is created with:
* Python version: 3.9.7
* JavaScript
* HTML&CSS
* Flask
* Tensorflow & Keras
	
## Setup
Model for brain detection is too large, but you can download this model from [link](https://www.dropbox.com/s/wj4op44hc20fszb/model_brain.h5?dl=0) and put in the "model" folder.
To run this project:

```
$ git clone https://github.com/UnknownC3PO/brain_tumor_detection.git
$ cd /home/user/brain_tumor_detection
$ python3 -m venv venv
$ source /home/user/brain_tumor_detection/venv/bin/activate
& pip install -r requirements.txt
$ python app.py
