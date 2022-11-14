from backend.types import UniqueViewsDocument
from backend.github_client import fetch_github_unique_views
from typing import List
from dotenv import load_dotenv
from pymongo import MongoClient
import os
load_dotenv()

class MongoDbAdapter():
    def __init__(self):
        self.mongo_client=None
        data=fetch_github_unique_views()
        self.store_data(data=data)
        
    def get_client(self):
        # Add your code here to create a mongo db client
        # that can read and write data from github_stats collection
        MONGO_URI=os.getenv("MONGO_URI")
        client = MongoClient(MONGO_URI)
        self.mongo_client=client['github_stats']
        pass

    def get_data(self) -> List[UniqueViewsDocument]:
        # Add your code here to read data from github_stats collection
        collection_name = self.mongo_client["visitors"]
        item_details = collection_name.find()
        return item_details
    
    def store_data(self, data: List[UniqueViewsDocument]):
        # Add your code here to store data in github_stats collection
        # Save each entry in the data list as a mongodb document
        self.get_client()
        collection_name=self.mongo_client["visitors "]
        collection_name.insert_many(data)
        pass
