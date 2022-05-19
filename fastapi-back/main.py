# Importation des modules fastapi
from cmath import log
from operator import index
from typing import Optional, Union
import bcrypt
from fastapi import FastAPI, Response, Request
from tables import Description
import uvicorn
import json
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class User(BaseModel):
    username: Union[str, None] = None
    nom: Union[str, None] = None
    prenom: Union[str, None] = None
    mail: Union[str, None] = None
    motDePasse: Union[str, None] = None
    confMotDePasse: Union[str, None] = None
    description: Union[str, None] = None
    banner: Union[str, None] = None
    check: bool


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
                        password, user["motDePasse"]):
                    return user
                else:
                    response.status_code = 404
                    return False
        response.status_code = 404
        return "User not found "


@app.post("/addUser")
def add_user(user: Request, filename="./JSON/Users.json"):
    print("Requete")
    # data = json.loads(user)
    # # user = {
    # #     "id": int,
    # #     "username": user.username,
    # #     "nom": user.nom,
    # #     "prenom": user.prenom,
    # #     "motDePasse": user.motDePasse,
    # #     "email": user.email,
    # #     "description": user.description,
    # #     "banner": user.banner
    # # }
    # # Load the json a file
    # with open(filename, "r+") as file:
    #     # Extract data in json
    #     data = json.load(file)
    #     # Extract last ID
    #     ID = 0
    #     for temp in data["users"]:
    #         ID = temp["id"]
    #         if(temp["username"] == user["username"]):
    #             return "Username Error"
    #         if(temp["username"] == user["username"]):
    #             return "Mail Error"

    #     # Set the next ID for the user
    #     user["id"] = ID+1
    #     # Hash the password
    #     user["motDePasse"] = set_hashed_password(user["motDePasse"])
    # # Append the new user data
    #     data["users"].append(user)
    #     file.seek(0)
    #     # Convert into JSON
    #     json.dump(data, file, indent=3)


@app.put("/modUser/{username}")
def mod_user(
        username,
        password,
        nom: Optional[str] = None,
        prenom: Optional[str] = None,
        description: Optional[str] = None):
    #
    i = 1
    with open("./JSON/Users.json") as file:
        data = json.load(file)
        for user in data["users"]:
            if user["username"] == username and verify_hashed_password(
                    password, user["motDePasse"]):
                if description != " " and description != user["username"]:
                    user["description"] = description
                if nom != None and nom != user["nom"]:
                    user["nom"] = nom
                if prenom != None and prenom != user["prenom"]:
                    user["prenom"] = prenom

    with open("./JSON/Users.json", "w") as file:
        json.dump(data, file, indent=3)


@app.delete("/delUser/{username}")
def del_user(username, password):
    i = 1
    with open("./JSON/Users.json") as file:
        # Extract JSON
        data = json.load(file)
        # Seacrch user
        for user in data["users"]:
            if user["username"] == username and verify_hashed_password(
                    password, user["motDePasse"]):
                data["users"].pop(i-1)
                break
            i = i+1

    with open("./JSON/Users.json", "w") as file:
        json.dump(data, file, indent=3)


    # Choix du port d'execution de notre API
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=2002)
