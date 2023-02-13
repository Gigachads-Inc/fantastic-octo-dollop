
from fastapi import FastAPI
import json
from pydantic import BaseModel

import redis

from typing import Optional

import pickle

rd = redis.Redis(host="localhost", port=6379, db = 0)

app = FastAPI()

class User(BaseModel):
    name: str
    github: Optional[str] = None
    twitch: Optional[str] = None
    phone: Optional[str] = None

@app.get("/")
def main_page():
    return {"s": "hello"}

@app.get("/search/{username}")
def show_contacts(username : Optional[str] = None):
    
    result = rd.get(username)

    if result:
        print(f"Contact: {username}")
        return pickle.loads(result)
    else:
        print("Contact not found")
        return {"Err" : "Contact does not exist"}

@app.post("/add_contact/")
def add_contacts(info: User):
    print("succesfull add some values")
    if rd.get(info.name) == None:
        p_value = pickle.dumps({"phone": info.phone, "github" : info.github, "twitch": info.twitch})
        rd.set(info.name, p_value)
        return {"msg" : "New contact has created"}
    else:
        return {"Err" : "Contact already used"}
