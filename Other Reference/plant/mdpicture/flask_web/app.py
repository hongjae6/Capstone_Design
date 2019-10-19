from fastai import *
from fastai.vision import *

from pathlib import Path

from flask import Flask

app = Flask(__name__)

IMAGE_PATH = 'image'
MODEL_PATH = 'model'
MODEL_NAME = 'stage-6'


def analysis():

    return 0



@app.route('/')
def main_index():
    return 'Hello World!'

@app.route('upload')
def file_upload():
    return 'Upload Complete!'


if __name__ == '__main__':
    app.run()
