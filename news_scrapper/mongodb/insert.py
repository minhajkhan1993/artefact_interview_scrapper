from mongodb.mongodb import MongoDB


def insert_article(mongodb: MongoDB, database: str, collection: str, article: dict):
    mongodb.set_db(database)
    mongodb.set_collection(collection)

    result = mongodb.insert_document(article)

    return result