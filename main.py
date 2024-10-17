from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/apple")
def read_apple():
    return "<p>Hello apple</p>"