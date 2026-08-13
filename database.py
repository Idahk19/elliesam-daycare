from pymongo import MongoClient
from dotenv import load_dotenv # use it read values on the .env
import os # use it to retrieve MONGO_URI

load_dotenv()

mongo_url = os.getenv("MONGO_URI")

client = MongoClient(mongo_url)

db = client["elliesam_daycare"] 

staff_collection = db["staff"]

# testing
try:
    client.admin.command("ping")
    print("Connection successful")
except Exception as e:
    print("Connection failed", e)