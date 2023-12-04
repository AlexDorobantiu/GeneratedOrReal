import json

from pydantic import BaseModel
from random import randint
from typing import List

from app.logic.images import get_image_paths

NO_MORE_IMAGES = 'No more images!'

FROM_NAME = "from_name"
BRUSH_TAGGING = "brush_tagging"


class Answer(BaseModel):
    image_path: str
    answer: dict


class Answers(BaseModel):
    name: str
    answers: List[Answer]
    

def get_next_image(username: str):
    try:
        answers = load_data(username)
    except FileNotFoundError:
        answers = Answers(name=username, answers=[])
    
    existing_files = get_image_paths()
    if not existing_files:
        return NO_MORE_IMAGES
    for answer in answers.answers:
        if answer.image_path in existing_files:
            existing_files.remove(answer.image_path)
    if not existing_files:
        return NO_MORE_IMAGES
    return existing_files[randint(0, len(existing_files) - 1)]


def persist_answer(username: str, image_path: str, array_answer: list):
    try:
        answers = load_data(username)
    except FileNotFoundError:
        answers = Answers(name=username, answers=[])

    dict_answer = {}
    brush = None
    for option in array_answer:
        if option[FROM_NAME] == BRUSH_TAGGING:
            brush = option
        else:
            dict_answer[option[FROM_NAME]] = option

    answers.answers.append(Answer(image_path=image_path, answer=dict_answer))
    with open(_create_filename(answers.name), "w") as f:
        json.dump(answers.model_dump(), f)
    if brush:
         with open(_create_filename(f"{answers.name}_{image_path}_brush"), "w") as f:
            json.dump(brush, f)


def _sanitize_filename(name: str) -> str:
    return "".join([c for c in name if c.isalnum() or c in {"-", "_", '.', ' '}])

def _create_filename(name: str) -> str:
    return f"/results/{_sanitize_filename(name)}.json"
   

def load_data(name: str) -> Answers:
    filename = _create_filename(name)
    with open(filename, "r") as f:
        data_dict = json.load(f)
    return Answers(**data_dict)
