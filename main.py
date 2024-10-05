from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"message" : "hello world!"}

@app.get('/items/{item_id}')
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"response" : item_id, "q" : q}