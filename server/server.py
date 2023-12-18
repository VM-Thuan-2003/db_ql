from typing import Union
from uvicorn import run

from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from fastapi.middleware.cors import CORSMiddleware


import json 
from bson import json_util

import user as d_user

uri = "mongodb+srv://admin:admin@dbgym.pvukikw.mongodb.net/?retryWrites=true&w=majority"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = MongoClient(uri)
app.client = MongoClient(uri, server_api=ServerApi('1'))
app.collection = app.client["db_user"]["user"]

try:
    client.admin.command('ping')
    print("You successfully connected to MongoDB!")
except Exception as e:
    print("Error is: ", e)

class User(BaseModel):
    fullName    : str
    address     : str
    subject     : str
    tax         : str
    description : Union[str, None] = "None Description"
    cost        : Union[int, None] = 0

@app.get("/test")
async def root():
    return {"message": "Hello World"}

@app.post("/user/new")
async def root(user: User):
    newUser = d_user.user(user, app.collection)
    payload = newUser.new_user()
    if(payload["status"] == True):
        app.collection.insert_one({
            "fullName":      payload["buffer"]["fullName"],
            "address":       payload["buffer"]["address"],
            "subject":       payload["buffer"]["subject"],
            "tax":           payload["buffer"]["tax"],
            "description":   payload["buffer"]["description"],
            "cost":          payload["buffer"]["cost"],
            "msg" :          payload["msg"],
            "time_create_user":          payload["time_create_user"]
        })
        return payload
    else:
        return payload
@app.post("/user/edit")
async def root(user: User):
    print(user)
    return {"message": "edit user"}

@app.post("/user/remove")
async def root(user: User):
    print(user)
    return {"message": "remove user"}

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=80)