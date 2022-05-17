# Importation des modules fastapi
from operator import index
from typing import Optional, Union
from fastapi import FastAPI, Response
import uvicorn
import json

# create object of FastAPI class
app = FastAPI()
# Open the data file
file = open('./JSON/Users.json')
# Extract data in json
data = json.load(file)


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
    for user in data["users"]:
        if(user["username"] == username):
            return user
    response.status_code = 404
    return "User not found "


@app.post("/addUser")
def add_user(username, nom, prenom, motDePasse, email, filename="./JSON/Users.json"):
    user = {
        "id": int,
        "username": username,
        "nom": nom,
        "prenom": prenom,
        "motDePasse": motDePasse,
        "email": email
    }
    # Load the json a file
    with open(filename, "r+") as file:
        # Extract data in json
        data = json.load(file)
        # Extract last ID
        ID = 0
        for temp in data["users"]:
            ID = temp["id"]
            if(temp["username"] == user["username"]):
                return "Username Error"
            if(temp["username"] == user["username"]):
                return "Mail Error"

        # Set the next ID for the user
        user["id"] = ID+1
    # Append the new user data
        data["users"].append(user)
        file.seek(0)
        # Convert into JSON
        json.dump(data, file, indent=3)


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
            if user["username"] == username and user["motDePasse"] == password:
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
            if user["username"] == username and user["motDePasse"] == password:
                data["users"].pop(i-1)
                break
            i = i+1

    with open("./JSON/Users.json", "w") as file:
        json.dump(data, file, indent=3)

    # Choix du port d'execution de notre API
    # if __name__ =="__main":
    #     uvicorn.run(app, host="0.0.0.0", port=2002)
