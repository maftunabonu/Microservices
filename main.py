from fastapi import FastAPI
import uvicorn
from mylib.logic import wiki, phrase

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Wikipedia api"}


@app.get("/search/{value}")
def search(value: str):
    result = wiki(value)
    return {"result": result}


@app.get("/phrases/{name}")
def phrases(name: str):
    wiki_phrases = phrase(name)
    return {"result": wiki_phrases}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
