import json
from typing import List
from pydantic import BaseModel

class Answer(BaseModel):
    image_path: str
    answer: dict

class Answers(BaseModel):
    name: str
    answers: List[Answer]

def save_data(data: Answers):
    filename = f"{data.name}.json"
    with open(filename, "w") as f:
        json.dump(data.model_dump(), f)

def load_data(name: str) -> Answers:
    filename = f"{name}.json"
    with open(filename, "r") as f:
        data_dict = json.load(f)
    return Answers(**data_dict)
