# Importation des modules necessaire au lancement du serveur
from fastapi import FastAPI

# Lancement de notre application
app = FastAPI()

# Declaration des middelwares


@app.get("/")
def Hello():
    return {"message": "Hello World"}
