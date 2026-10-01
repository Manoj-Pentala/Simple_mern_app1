from fastapi import FastAPI
from models import Student,Staff
from database import staff_collection,student_collection


app=FastAPI()
def student_details(Student):
    return{
        "id":str(Student["_id"]),
        "name":Student["name"],
        "email":Student["email"],
        "age":Student["age"],
        "mark":Student["mark"]
    }
def staff_details(Staff):
    return{
        "id":str(Staff["_id"]),
        "name":Staff["name"],
        "email":Staff["email"],
        "designation":Staff["designation"]
    }
#STUDENT
@app.get("/getstudents")
def getstudents():
    students=student_collection.find()
    return [student_details(student) for student in students]

# student register
@app.post("/register")
def register(stu:Student):
    result=student_collection.insert_one(stu.model_dump())
    return {"message":"data is inserted"}




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

#================================satff ===================================

@app.get("/getstaff")
def getstaff():
    staffs=staff_collection.find()
    return [staff_details(staff) for staff in staffs]


@app.post("/staffregister")
def register(stu:Staff):
    result=staff_collection.insert_one(stu.model_dump())
    return {"message":"data is inserted"}
