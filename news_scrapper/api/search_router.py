from fastapi import APIRouter
from mongodb.mongodb import MongoDB
import mongodb.search as searchModule
import os


mongo_router = APIRouter()


@mongo_router.get("/{key_word}")
def search(key_word: str) -> dict:
    mongo_instance = MongoDB()
    mongo_instance.createMongoClient(os.environ.get('MONGODB_URL'))

    result = searchModule.search(mongo_instance, os.environ.get('Mongo_Document'), os.environ.get('Mongo_Collection'), key_word)

    return_list = []
    return_object = {}

    for row in result:
        return_list.append(row)
    
    return_object['search_result'] = return_list

    return return_object


@mongo_router.get("/headline/{key_word}")
def search_headline(key_word: str) -> dict:
    mongo_instance = MongoDB()
    mongo_instance.createMongoClient(os.environ.get('MONGODB_URL'))

    result = searchModule.search_headline(mongo_instance, os.environ.get('Mongo_Document'), os.environ.get('Mongo_Collection'), key_word)

    return_list = []
    return_object = {}

    for row in result:
        return_list.append(row)
    
    return_object['search_result'] = return_list

    return return_object


@mongo_router.get("/article_body/{key_word}")
def search_article_body(key_word: str) -> dict:
    mongo_instance = MongoDB()
    mongo_instance.createMongoClient(os.environ.get('MONGODB_URL'))

    result = searchModule.search_article_body(mongo_instance, os.environ.get('Mongo_Document'), os.environ.get('Mongo_Collection'), key_word)

    return_list = []
    return_object = {}

    for row in result:
        return_list.append(row)
    
    return_object['search_result'] = return_list

    return return_object