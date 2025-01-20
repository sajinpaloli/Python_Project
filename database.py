import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
def get_data():
    client = MongoClient(MONGO_URI)
    db = client['python']  # Database name
    collection = db['sample']  # Collection name
    return collection

 
    

