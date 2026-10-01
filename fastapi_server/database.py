#it holds the information about db and colection

from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
client=MongoClient(os.getenv("mongo_url"))
db=client["vignan"]    #create a database in db
student_collection=db["student"]
staff_collection=db["staff"]


