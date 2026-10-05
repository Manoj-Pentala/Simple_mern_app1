from fastapi import APIRouter
from models import Staff
from database import staff_collection

def staff_details(Staff):
    return{
        "id":str(Staff["_id"]),
        "name":Staff["name"],
        "email":Staff["email"],
        "designation":Staff["designation"]
    }

staff_router=APIRouter(prefix='/staff',tags=["staff"])
@staff_router.get("/getStaffs")
def getStaffs():
    return "get staff method called"

@staff_router.post("/addstaff")
def addstaff():
    return "add staff method called"