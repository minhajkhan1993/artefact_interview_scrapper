from mongodb.mongodb import MongoDB
import re



# search keyword both in headline and body content
def search(connection_url: str, database: str, collection: str, keyword: str):

    # get headline that contains the keyword
    headline_result = search_headline(connection_url, database, collection, keyword)
    headline_result_list = [result for result in headline_result]

    # get results of search article body that are not in headline search result  
    headline_result_urls = [result['url'] for result in headline_result_list]
    article_body_result = search_article_body(connection_url, database, collection, keyword)
    article_body_result_without_headline_result = [result for result in article_body_result if result['url'] not in headline_result_urls]
    
    result_to_return = headline_result_list + article_body_result_without_headline_result

    return result_to_return



# search keyword in headline
def search_headline(connection_url: str, database: str, collection: str, keyword: str):
    
    mongo_instance = MongoDB()
    mongo_instance.create_mongo_client(connection_url)
    
    mongo_instance.set_db(database)
    mongo_instance.set_collection(collection)

    # build regex using the keyword. The regex looks for whole word within the text to be searched
    regx = re.compile(r"\b" + re.escape(keyword) + r"\b", re.IGNORECASE)
    query_condition = {"headline": regx}

    result = mongo_instance.find_document(query_condition)

    return result


# search keyword in page body
def search_article_body(connection_url: str, database: str, collection: str, keyword: str):
    
    mongo_instance = MongoDB()
    mongo_instance.create_mongo_client(connection_url)
    
    mongo_instance.set_db(database)
    mongo_instance.set_collection(collection)

    # build regex using the keyword. The regex looks for whole word within the text to be searched
    regx = re.compile(r"\b" + re.escape(keyword) + r"\b", re.IGNORECASE)
    query_condition = {"body": regx}

    result = mongo_instance.find_document(query_condition)

    return result


