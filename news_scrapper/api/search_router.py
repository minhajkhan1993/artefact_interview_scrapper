from fastapi import APIRouter
from mongodb.mongodb import MongoDB
import mongodb.search as searchModule
import os


mongo_router = APIRouter()


# endpoint that searches for keyword in both headline and page body content
@mongo_router.get("/{key_word}")
def search(key_word: str) -> dict:

    result = searchModule.search(os.environ.get('MONGODB_URL'), os.environ.get('Mongo_Database'), os.environ.get('Mongo_Collection'), key_word)

    return_list = result
    return_object = {}
    
    return_object['search_result'] = return_list

    return return_object


# endpoint that searches for keyword in page headline
@mongo_router.get("/headline/{key_word}")
def search_headline(key_word: str) -> dict:

    result = searchModule.search_headline(os.environ.get('MONGODB_URL'), os.environ.get('Mongo_Database'), os.environ.get('Mongo_Collection'), key_word)

    return_list = []
    return_object = {}

    for row in result:
        return_list.append(row)
    
    return_object['search_result'] = return_list

    return return_object


# endpoint that searches for keyword in page body content
@mongo_router.get("/article_body/{key_word}")
def search_article_body(key_word: str) -> dict:

    result = searchModule.search_article_body(os.environ.get('MONGODB_URL'), os.environ.get('Mongo_Database'), os.environ.get('Mongo_Collection'), key_word)

    return_list = []
    return_object = {}

    for row in result:
        return_list.append(row)
    
    return_object['search_result'] = return_list

    return return_object