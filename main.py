from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': 'Hello world!'}

@app.get('/about')
def about():
    return {'data': 'about page'}