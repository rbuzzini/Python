from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
import os
from typing import Optional
os.getcwd()

try:
    os.chdir(r'.\FastAPI')
except:
    pass

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # optional field with default value=True
    rating: Optional[int] = None # fully optional field

@app.get("/")
async def root():
    return {"message": "Hello World!!!"}

@app.get("/posts")
def gest_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    print(new_post.dict())
    return {"data": "new post"}
# we expect the user to insert these things: 
# title str, content str nothing else.
# We can also include category, Bool published etc.