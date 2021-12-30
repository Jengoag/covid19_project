from fastapi import FastAPI

app = FastAPI()

# endpoint de inicio 
@app.get("/")
def root():
    return {"Holi!"}

@app.get("/covid")
def root():
    return {"Fucking Covid"}



@app.post("/")
def root():
    return {"request":"POST"}


@app.get("/hello/{name}")
def salute(name):
    return {"message":f"Hello, {name}"}

@app.get("/person/{name}/{age}")
def person(name: str, age: int):
    item = {
        "name" : {
            "value": name,
            "type": str(type(name))
        },
        "age" : {
            "value": age,
            "type": str(type(age))
        }
    }
    return item

@app.get("/sum")
def suma(a:int=0, b:int=0):
    return {"result":a+b}