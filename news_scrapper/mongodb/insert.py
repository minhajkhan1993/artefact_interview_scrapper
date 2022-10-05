from mongodb.mongodb import MongoDB


# inserts the provided article object into the mongodb collection specified by the args. 
def insert_article(connection_url: str, database: str, collection: str, article: dict):
    
    # create mongodb client
    mongo_instance = MongoDB()
    mongo_instance.create_mongo_client(connection_url)
    
    # set client to point to specified database and collection
    mongo_instance.set_db(database)
    mongo_instance.set_collection(collection)

    # submit article to mongodb's insert function
    result = mongo_instance.insert_document(article)

    return result