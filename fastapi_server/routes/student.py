from fastapi import APIRouter
from models import Student
from database import student_collection
from bson import ObjectId

def student_details(Student):
    return{
        "id":str(Student["_id"]),
        "name":Student["name"],
        "email":Student["email"],
        "age":Student["age"],
        "mark":Student["mark"]
    }

student_router=APIRouter(prefix='/student',tags=["student"])


@student_router.get("/getstudents")
def getstudents():
    students=student_collection.find()
    return [student_details(student) for student in students]

@student_router.post("/register")
def register(stu:Student):
    result=student_collection.insert_one(stu.model_dump())
    return {"message":"data is inserted"}


@student_router.get("/getparticularstudent/{stuid}")
def getparticularstudent(stuid:str):
    student=student_collection.find_one({
        "_id":ObjectId(stuid)
    })
    return student_details(student)


@student_router.delete("/deletestudent/{stuid}")
def deletestudent(stuid:str):
    result=student_collection.delete_one({
        "_id":ObjectId(stuid)
    })
    return "student delete sucessfully"

@student_router.put("/updatestudent/{stuid}")
def updatestudent(stuid:str,stu:Student):
    result=student_collection.update_one(
        {"_id":ObjectId(stuid)},
        {"$set":stu.model_dump()}
        )
    return "student updated sucessfully"