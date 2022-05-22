# Importation des modules fastapi
# from cmath import log
# from operator import index
from email import message
from fileinput import filename
from typing import Optional, Union
import bcrypt
from fastapi import FastAPI, Response, Request
from sqlalchemy import true
# from requests import delete, request
# from tables import Description
import uvicorn
import json
from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import asyncio


def set_hashed_password(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())


def verify_hashed_password(text_password, hashed_password):
    return bcrypt.checkpw(text_password, hashed_password)


# create object of FastAPI class
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def main():
    return {"body": "Hello"}


@app.get("/users")
def read_users():
    with open("./JSON/Users.json") as file:
        dataToJSON = json.load(file)
    return dataToJSON["users"]


@app.get("/user/{username}")
def read_user(username, response: Response):
    with open('./JSON/Users.json') as file:
        dataToJSON = json.load(file)
        for user in dataToJSON["users"]:
            if(user["username"] == username):
                del user["motDePasse"]
                del user["id"]
                return user
        response.status_code = 404
        return "User not found "


@app.get("/login/{username}")
def log_user(username, password, response: Response):
    with open('./JSON/Users.json') as file:
        dataToJSON = json.load(file)
        for user in dataToJSON["users"]:
            if(user["username"] == username):
                if verify_hashed_password(
                        password.encode("utf-8"), user["motDePasse"].encode("utf-8")):
                    return user
                else:
                    response.status_code = 404
                    return False
        response.status_code = 404
        return "User not found "


@app.post("/addUser")
async def add_user(request: Request, response: Response):
    dataReceive = await request.json()
    filename = "./JSON/Users.json"
    user = {
        "id": int,
        "username": dataReceive["username"],
        "nom": dataReceive["nom"],
        "prenom": dataReceive["prenom"],
        "motDePasse": dataReceive["motDePasse"],
        "email": dataReceive["email"],
        "description": dataReceive["description"],
        "banner": dataReceive["banner"]
    }
    # # Load the json a file
    with open(filename, "r+") as file:
        # Extract data in json
        data = json.load(file)
        # Extract last ID
        ID = 0
        for temp in data["users"]:
            ID = temp["id"]
            if(temp["username"] == user["username"]):
                response.status_code = 404
                return "Username Error"
            if(temp["username"] == user["username"]):
                response.status_code = 404
                return "Mail Error"
        # user = json.dumps()
        # Set the next ID for the user
        user["id"] = ID+1
        # Hash the password
        user["motDePasse"] = set_hashed_password(
            user["motDePasse"].encode("utf-8"))

        user["motDePasse"] = user["motDePasse"].decode("utf-8")
        # # Append the new user data
        data["users"].append(user)
        file.seek(0)
        # # Convert into JSON
        json.dump(data, file, indent=3)


@app.put("/modUser/{username}")
def mod_user(
        username,
        password,
        nom: Optional[str | None] = None,
        prenom: Optional[str | None] = None,
        description: Optional[str | None] = None):
    i = 1
    B = {
        "description": "",
        "nom": "",
        "prenom": ""
    }
    with open("./JSON/Users.json") as file:
        data = json.load(file)
        for user in data["users"]:
            if user["username"] == username and password == user["motDePasse"]:
                B["description"] = user["description"]
                B["nom"] = user["nom"]
                B["prenom"] = user["prenom"]

                if description != None and description != user["description"]:
                    user["description"] = description
                    B["description"] = description
                if nom != None and nom != user["nom"]:
                    user["nom"] = nom
                    B["nom"] = nom
                if prenom != None and prenom != user["prenom"]:
                    user["prenom"] = prenom
                    B["prenom"] = prenom
    with open("./JSON/Users.json", "w") as file:
        json.dump(data, file, indent=3)

    return B


@app.delete("/delUser/{username}")
def del_user(username, password):
    i = 1
    with open("./JSON/Users.json") as file:
        # Extract JSON
        data = json.load(file)
        # Seacrch user
        for user in data["users"]:
            if user["username"] == username and password.encode("utf-8") == user["motDePasse"].encode("utf-8"):
                # if user["username"] == username and verify_hashed_password(
                #     password.encode("utf-8"), user["motDePasse"].encode("utf-8")):
                data["users"].pop(i-1)
                break
            i = i+1

    with open("./JSON/Users.json", "w") as file:
        json.dump(data, file, indent=3)


@app.get("/getMessages/{id}")
async def get_message(id):
    last_update = []
    ID = int(id)
    filename = "./JSON/Messages.json"
    # Load the json a file
    with open(filename, "r+") as file:
        # Extract data in json
        data = json.load(file)
        # Extract new ID
        for message in data['messages']:
            if(message["id"] > ID):
                # print(message)
                last_update.append(message)
    return last_update


@app.post("/sendMessage")
async def post_message(request: Request):
    dataReceive = await request.json()
    filename = "./JSON/Messages.json"
    # print(dataReceive)
    message = {
        "id": int,
        "content": dataReceive["content"],
        "sender": dataReceive["username"]
    }

    # # Load the json a file
    with open(filename, "r+") as file:
        # Extract data in json
        data = json.load(file)
        # Extract last ID
        ID = 0
        for temp in data["messages"]:
            ID = temp["id"]
        message["id"] = ID+1
        # # Append the new user data
        data["messages"].append(message)
        file.seek(0)
        # # Convert into JSON
        json.dump(data, file, indent=3)

    return true

    # Choix du port d'execution de notre API
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
