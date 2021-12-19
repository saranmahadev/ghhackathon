import pymongo
import os

class Db:
    def __init__(self,collection) -> None:
        DB_CONNECTION_STRING = os.environ['DB_CONNECTION_STRING']
        self.client = pymongo.MongoClient(DB_CONNECTION_STRING)
        self.db = self.client.get_database('ghhndb')
        self.collection = self.db.get_collection(collection)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()

    def insert(self,data) -> bool:
        try:
            self.collection.insert_one(data)
            return True
        except:
            return False
    
    def find(self,query) -> list:
        try:
            return self.collection.find_one(query)
        except:
            return []
    
    def findall(self) -> list:
        try:
            return list(self.collection.find())
        except:
            return []

    def update(self,query,data) -> bool:
        try:
            self.collection.update_one(query,data)
            return True
        except:
            return False
    
    def delete(self,query) -> bool:
        try:
            self.collection.delete_one(query)
            return True
        except:
            return False