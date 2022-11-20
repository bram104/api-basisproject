from fastapi import FastAPI
import json
import random

with open("../lijst.json") as dranken:
    lijst = json.load(dranken)


app = FastAPI()


@app.get("/bieren")
async def read_item():
    return lijst["bieren"][0]["bierId"]


@app.get("/cocktails")
async def read_item():
    return random.choice(lijst["cocktails"])



