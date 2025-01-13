import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client['python']  # Database name
collection = db['sample']  # Collection name

def get_data():
    data = collection.find({}, {"_id": 0}).limit(5) 
    return list(data)
