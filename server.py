from fastapi import FastAPI

app = FastAPI()

@app.route('/')
def callback_api():
    return '726940b3'