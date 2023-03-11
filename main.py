from fastapi import FastAPI
from util.get_status import Get_Status
from models.status_model import Status_Model

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/GCP_Updates/{Location}")
async def read_item(Location: str)-> Status_Model:
    return Get_Status(Location)