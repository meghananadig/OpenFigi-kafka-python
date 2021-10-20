from fastapi import FastAPI
import app.repo as repo
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.on_event("startup")
def startup():
    repo.fastapi_connect()
    print("Connected to Postgres from Fast API")

@app.on_event("shutdown")
def shutdown():
    repo.disconnect()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/securities/{securityType}")
def getSecuritiesByType(securityType):
    result = repo.getSecurityByType(securityType)
    result = jsonable_encoder(result)
    return JSONResponse(content=result)