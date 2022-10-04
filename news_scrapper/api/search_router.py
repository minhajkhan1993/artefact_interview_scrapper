from fastapi import APIRouter

mongo_router = APIRouter()


@mongo_router.get("/{key_word}")
def search(key_word: str) -> str:
    ## implement search function
    return 'implement search function'


@mongo_router.get("/headline/{key_word}")
def search_headline(key_word: str) -> str:
    ## implement search function
    return 'implement search function'


@mongo_router.get("/article_body/{key_word}")
def search_article_body(key_word: str) -> str:
    ## implement search function
    return 'implement search function'