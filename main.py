from fastapi import FastAPI, Path

app = FastAPI()
@app.get('/')
def root():
    return {'message': 'Hello student'}

@app.get("/add")
def add(x: int, y : int) -> int:
    return x+y

@app.get("/double/{number}")
def double(number: int) -> int:
    return number*2

@app.get("/welcome/{name}")
def welcome(name: str = Path(min_length = 2, max_length =20)) -> str:
    return f"Good luck, {name}"

