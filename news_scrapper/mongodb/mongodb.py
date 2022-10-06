import pymongo
import os

class MongoDB():

    def create_mongo_client(self, conn_url):
        self.client = pymongo.MongoClient(conn_url)
    
    def set_db(self, db: str):
        self.db = self.client[db]

    def set_collection(self, collection: str):
        self.col = self.db[collection]

    def insert_document(self, document: dict):
        return self.col.insert_one(document)
    
    def find_document(self, condition: dict):
        return self.col.find(condition, {"_id": 0})
