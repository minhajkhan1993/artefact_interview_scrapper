from mongodb.mongodb import MongoDB


def insert_article(mongodb: MongoDB, database: str, collection: str, article: dict):
    mongodb.setDb(database)
    mongodb.setCollection(collection)

    result = mongodb.insertDocument(article)

    return result