from fastapi import FastAPI
from pydantic import BaseModel
class Student(BaseModel):
    name:str
    email:str
    age:int
    mark:float


app=FastAPI()
@app.get("/getstudents")
def getstudents():
    return "get students api called"
@app.post("/register")
def register(stu:Student):
    return stu



@app.put("/updateprofile")
def updateprofile():
    return "update profile is called"

@app.delete("/delete")
def delete():
    return "delete page is called"

@app.get("/getstudentDet/{userid}")
def getstudentDet(userid:int):
    return {"user_id":userid}    


@app.get("/getstudentsdetails")
def getstudentsdetails(page:int=1,limit:int=10):
    return {"page":page,"limit":limit}

