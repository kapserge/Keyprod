import json
import os
from typing import Literal, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
import random
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from mangum import Mangum
from fastapi import FastAPI, Response, responses

####### ----Create class  Model

class Produit(BaseModel):
    name:str
    poid: float
    version : str

class Commande(BaseModel):
    
    commande_id: Optional[str] = uuid4().hex
    name_client: str
    status: Literal["en-traitement", "envoyer","en-cours-de-livraison","livrer"]
    date: str
    produits: list[Produit]| None = None

    
###### -----Open file----

COMMANDE_FILE = "commandes.json"
COMMANDE = []

PRODUIT_FILE = "produits.json"
PRODUIT = []

if os.path.exists(COMMANDE_FILE):
    with open(COMMANDE_FILE, "r") as f:
        COMMANDE = json.load(f)

elif os.path.exists(PRODUIT_FILE):
    with open(PRODUIT_FILE, "r") as jj:
        PRODUIT = json.load(jj)

app = FastAPI()

handler = Mangum(app)

######----- fonction home 
@app.get("/")
async def root():
    return {"message": "Welcome to keyprod!"}

######----- list commande
@app.get("/list-commandes")
async def list_commandes():
    return {"commandes": COMMANDE}

######----- detail commande

@app.get("/get-commande")
async def get_commande(commande_id: str):
    for commande in COMMANDE:
        if commande["commande_id"] == commande_id:
            return commande

    raise HTTPException(404, f"COMMANDE ID {commande_id} not found in database.")

######----- update status commande

@app.put("/update-commande/{commande_id}")
async def update_commande(commande_id: str, new_todo: Commande):
    try:
        for commande in COMMANDE:
            if commande["commande_id"] == commande_id:
                
                commande["commande_id"]== new_todo
            
        return commande
    except:
        raise HTTPException(404, f"COMMANDE ID {commande_id} not found in database.")


######----- search commande par date et status

@app.get("/commande/search")
def index(date,status , response: Response):
    founded_commande = [commande for commande in COMMANDE if date.lower()   in commande["date"].lower()]
    founded_commande = [commande for commande in founded_commande if status.lower()   in commande["status"].lower()]
    if not founded_commande: 
        response.status_code = 404
        return "No Products Found"

    return founded_commande if len(founded_commande) > 1 else founded_commande[0]


######----- add commande 
@app.post("/add-commande")
async def add_commande(commande: Commande):
    commande.commande_id = uuid4().hex
    json_commande = jsonable_encoder(commande)
    COMMANDE.append(json_commande)

    with open(COMMANDE_FILE, "w") as f:
        json.dump(COMMANDE, f)

    return {"commande_id": commande.commande_id}

#############----Produits

######----- list produits 
@app.get("/list-produits")
async def list_produits():
    return {"produits": PRODUIT}

######----- detail produits 
@app.get("/get-produit")
async def get_commande(name: str):
    for produit in PRODUIT:
        if produit["name"] == name:
            return produit["poid"]

    raise HTTPException(404, f"Produit Name {name} not found in database.")

######----- add produits 
@app.post("/add-produit")
async def add_produit(produit: Produit):
    
    json_produit = jsonable_encoder(produit)
    PRODUIT.append(json_produit)

    with open(PRODUIT_FILE, "w") as f:
        json.dump(PRODUIT, f)

    return {"produit_name": produit.name}

