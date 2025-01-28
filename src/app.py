from fastapi import FastAPI

app = FastAPI()
@app.get('/')
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run()