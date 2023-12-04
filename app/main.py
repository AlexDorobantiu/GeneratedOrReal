import json
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from app.logic.next_image import get_next_image, persist_answer
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

random_guid="9e0a8953-92d7-428e-97f5-e94f8ef5fef2" 

app.mount(f"/{random_guid}/", StaticFiles(directory="app/static"), name="static")

@app.get("/9e0a8953-92d7-428e-97f5-e94f8ef5fef3/next-image/{username}", response_class=PlainTextResponse)
def next_image(username: str):
    return get_next_image(username)


class AnwerBody(BaseModel):
    answer: str

@app.post("/9e0a8953-92d7-428e-97f5-e94f8ef5fef3/save-answer/{username}/{image_path}")
def save_answer(username: str, image_path: str, answer_body: AnwerBody):
    array_answer = json.loads(answer_body.answer)
    return persist_answer(username, image_path, array_answer)
