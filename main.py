from fastapi import FastAPI, Body, Depends
import schemas
import models

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)  # create database

#access the database
def get_session():
    session = SessionLocal()
    try:
        yield session

    finally:
        session.close()

app = FastAPI()

fakeDatabase = {
    1 : {'task' : 'Clean Car'},
    2 : {'task' : 'Write code'},
    3 : {'task' : 'Start sleeping'},

}

@app.get("/")
def getItems(session : Session = Depends(get_session)): # gives access to the database
    items = session.query(models.Item).all()
    return items

@app.get("/{id}")
def getSingleItem(id : int):       # id needs to be int only
    return fakeDatabase[id]

# @app.post("/")
# def addItems(task : str):        # we want task from body and needs to be string only
#     newId = len(fakeDatabase.keys()) + 1
#     fakeDatabase[newId] = {'task' : task}  # jo req se task aa rha hai usko fakedb mei daal rhe hai
#     return fakeDatabase


# @app.post("/")
# def addItems(item : schemas.Item):      # schema file ke andr Item Class  => item ek class ka object bnn gya  
#     newId = len(fakeDatabase.keys()) + 1
#     fakeDatabase[newId] = {'task' : item.task} #Item.task
#     return fakeDatabase

@app.post("/")
def addItems(body = Body()):      # schema file ke andr Item Class  => item ek class ka object bnn gya  
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {'task' : body['task']} #Item.task
    return fakeDatabase


@app.put("/{id}")   # yeh wali toh required field bnn jati hai
def updateItem(id: int, item : schemas.Item):   # item body vala hai
    fakeDatabase[id]['task'] = item.task
    return fakeDatabase

@app.delete("/{id}")
def deleteItem(id : int):
    fakeDatabase.pop(id)
    return fakeDatabase
