import json

import dill

import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
with open('model/sber_model.pickle', 'rb') as file:
    best_model = dill.load(file)


class Form(BaseModel):
    # session_id: str
    # hit_date: str
    # hit_time: float
    # hit_number: int
    # hit_type: str
    # hit_referer: str
    # hit_page_path: str
    # event_category: str
    # event_action: str
    # event_label: str
    # event_value: str
    # client_id: str
    # visit_date: str
    # visit_time: str
    # visit_number: int
    # device_model: str
    utm_source: str
    utm_medium: str
    utm_campaign: str
    utm_adcontent: str
    utm_keyword: str
    device_category: str
    device_os: str
    device_brand: str
    device_screen_resolution: str
    device_browser: str
    geo_country: str
    geo_city: str


class Prediction(BaseModel):
    Result: float


@app.get('/status')
def status():
    return "I'm OK"


@app.get('/version')
def version():
    return best_model['metadata']


@app.post('/predict', response_model=Prediction)
def predict(form: Form):
    df = pd.DataFrame.from_dict([form.dict()])
    y = best_model['model'].predict(df)

    return {
        'Result': y[0]
    }


