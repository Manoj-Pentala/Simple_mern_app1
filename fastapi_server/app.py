from fastapi import FastAPI
from routes.student import student_router
from routes.staff import staff_router

app=FastAPI()
app.include_router(student_router)
app.include_router(staff_router)



#STUDENT


# student register





# @app.put("/updateprofile")
# def updateprofile():
#     return "update profile is called"

# @app.delete("/delete")
# def delete():
#     return "delete page is called"

# @app.get("/getstudentDet/{userid}")
# def getstudentDet(userid:int):
#     return {"user_id":userid}    

# @app.get("/getstudentsdetails")
# def getstudentsdetails(page:int=1,limit:int=10):
#     return {"page":page,"limit":limit}

# #================================satff ===================================

# @app.get("/getstaff")
# def getstaff():
#     staffs=staff_collection.find()
#     return [staff_details(staff) for staff in staffs]


# @app.post("/staffregister")
# def register(stu:Staff):
#     result=staff_collection.insert_one(stu.model_dump())
#     return {"message":"data is inserted"}
