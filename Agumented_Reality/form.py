from flask import Flask
from flask import request
from flask import render_template
import cv2
import numpy as np


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html") # this should be the name of your html file

@app.route('/', methods=['POST'])
def ar():
    cap = cv2.VideoCapture(0)
    while True:
        ret, image = cap.read()
        cv2.imshow("Input", image)
        key = cv2.waitKey(3) & 0xFF

@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['text1']
    text2 = request.form['text2']
    plagiarismPercent = 51
    if plagiarismPercent > 50 :
        return "<h1>Plagiarism Detected !</h1>"
    else :
        return "<h1>No Plagiarism Detected !</h1>"

if __name__ == '__main__':
    app.run()