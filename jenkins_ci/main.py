from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import numpy as np
import pandas as pd 
from fastapi.middleware.cors import CORSMiddleware
from prediction_model.predict import generate_predictions

app =FastAPI(
    title='Loan prediction app using API - CI CD Jenkins',
    description= 'A simple CI CD',
    version='1.0'
)

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
async def index():
    return {'message':'Welcome to loan application App using API CI CD jenkins'}