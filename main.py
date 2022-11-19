from fastapi import FastAPI

app = FastAPI()

fakeDatabase = {
    1 : {'task' : 'Clean Car'},
    2 : {'task' : 'Write code'},
    3 : {'task' : 'Start sleeping'},

}

@app.get("/")
def getItems():
    return fakeDatabase

@app.get("/{id}")
def getSingleItem(id : int):       # id needs to be int only
    return fakeDatabase[id]

@app.post("/")
def addItems(task : str):        # we want task from body and needs to be string only
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {'task' : task}  # jo req se task aa rha hai usko fakedb mei daal rhe hai
    return fakeDatabase