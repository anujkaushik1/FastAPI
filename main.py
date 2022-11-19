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
def getSingleItem(id : int):
    return fakeDatabase[id]