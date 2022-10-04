import pymongo
import os

class MongoDB():

    def createMongoClient(self, conn_url):
        self.client = pymongo.MongoClient(conn_url)
    
    def setDb(self, db: str):
        self.db = self.client[db]

    def setCollection(self, collection: str):
        self.col = self.db[collection]

    def insertDocument(self, document: dict):
        self.col.insert_one(document)
    
    def findDocument(self, condition: dict):
        return self.col.find(condition, {"_id": 0})
