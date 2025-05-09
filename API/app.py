import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Alfonso", "Miriam", "Jonathan", "Veleza", "Ronald"]
    return rows


@app.get("/superheroesDC")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows

@app.get("/cursosPlatzi")
def get_cursosplatzi():
    rows = ["Docker", "Bash", "Linux", "Inglés", "Python", "Javascript", "Azure", "Github"]
    return rows