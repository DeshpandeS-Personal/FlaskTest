from flask import Flask,render_template, Response,request
import cv2
import sys
import json
import numpy as np
import time
import mediapipe as mp
import pafy

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
