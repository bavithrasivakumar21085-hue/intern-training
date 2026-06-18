from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def greeting():
    return "Welcome JSON"

@app.get("/hello/{name}")
def test(name:str):
    return f"hello. {name}, Welcome to FastAPI"


