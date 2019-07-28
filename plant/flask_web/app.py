from __future__ import division, print_function

from flask import Flask
from flask import render_template, request

from fastai import *
from fastai.vision import *
from PIL import Image as PILImage

import base64

app = Flask(__name__)

MODEL_FILE_NAME = 'stage-6'
PATH_TO_MODELS_DIR = Path('')
classes = ['UNKNOWN', 'UNKNOWN', 'Aglaonema',
 'Alocasia',
 'Aloe vera',
 'Anthurium',
 'Aphelandra squarrosa',
 'Araucaria heterophylla',
 'Asparagus aethiopicus',
 'Aspidistra elatior',
 'Begonia',
 'Bromeliaceae',
 'Calathea',
 'Cattleya',
 'Chamaedorea elegans',
 'Chlorophytum comosum',
 'Citrus',
 'Crassula ovata',
 'Crocus',
 'Cyclamen',
 'Cymbidium',
 'Dendrobium',
 'Dieffenbachia',
 'Dracaena',
 'Dypsislutescens',
 'Echeveria',
 'Epiphyllum',
 'Epipremnumaureum',
 'Ficusbenjamina',
 'Ficuselastica',
 'Ficuslyrata',
 'Gymnocalyciummihanovichii',
 'Haworthia',
 'Hederahelix',
 'Hippeastrum',
 'Hoya',
 'Hyacinthus',
 'Mammillaria',
 'Maranta',
 'Miltoniopsis',
 'Mimosapudica',
 'Monstera',
 'Narcissus',
 'Nephrolepis exaltata',
 'Oncidium',
 'Opuntia',
 'Paphiopedilum',
 'Philodendron',
 'Pilea peperomioides',
 'Saintpaulia',
 'Sansevieriatrifasciata',
 'Saxifragastolonifera',
 'Scheffleraarboricola',
 'Scindapsuspictus',
 'Seneciorowleyanuss',
 'Sinningiaspeciosa',
 'Spathiphyllum',
 'Stephanotisfloribunda',
 'Tradescantiazebrina',
 'Yucca',
 'Zygocactus']

def setup_model_pth(path_to_pth_file, learner_name_to_load, classes):
    data = ImageDataBunch.single_from_classes(
        path_to_pth_file, classes, ds_tfms=get_transforms(), size=224).normalize(imagenet_stats)
    learn = cnn_learner(data, models.resnet50, model_dir='models')
    learn.load(learner_name_to_load, device=torch.device('cpu'))
    return learn

learn = setup_model_pth(PATH_TO_MODELS_DIR, MODEL_FILE_NAME, classes)

def encode(img):
    img = (image2np(img.data) * 255).astype('uint8')
    pil_img = PILImage.fromarray(img)
    buff = BytesIO()
    pil_img.save(buff, format="JPEG")
    return base64.b64encode(buff.getvalue()).decode("utf-8")

def model_predict(img):
    img = open_image(BytesIO(img))
    pred_class, outputs = learn.predict(img)
    img_data = encode(img)

    result = {"class": pred_class, "image": img_data}
    return render_template('result.html', result = result)

@app.route('/', methods=['GET', "POST"])
def index():
    return render_template('index.html')

@app.route('/upload', methods=["POST", "GET"])
def upload():
    if request.method == 'POST':
        img = request.files['file'].read()
        if img != None:
            preds = model_predict(img)
            return preds
    return 'OK'

if __name__ == '__main__':
    app.run()
