from random import randint
from app.logic.images import get_image_paths

from app.logic.persistence import Answers, Answer, load_data, save_data

NO_MORE_IMAGES = 'No more images!'

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


def persist_answer(username: str, image_path: str, answer: dict):
    try:
        answers = load_data(username)
    except FileNotFoundError:
        answers = Answers(name=username, answers=[])
    answers.answers.append(Answer(image_path=image_path, answer=answer))
    save_data(answers)