from unittest import mock
import mongodb.search as search
import mongodb.insert as insert
from mongodb.mongodb import MongoDB
import os



def refresh_test_db():
    connection_string = os.environ.get('MONGODB_URL')
    
    mongo_instance = MongoDB()
    mongo_instance.create_mongo_client(connection_string)
    mongo_instance.client['test_db']['test_collection'].delete_many({})


def test_insert():
    refresh_test_db()
    
    connection_string = os.environ.get('MONGODB_URL')

    test_doc = {'url':'test_url','headline':'test headline','body':'test body'}

    assert insert.insert_article(connection_string,'test_db','test_collection',test_doc).acknowledged ==  True

    refresh_test_db()


def test_search_article_body():
    connection_string = os.environ.get('MONGODB_URL')
    assert len(list(search.search_article_body(connection_string,'test_db','test_collection','body')))  == 0

    test_doc = {'url':'test_url','headline':'test headline','body':'test body'}

    insert.insert_article(connection_string,'test_db','test_collection',test_doc)

    assert len(list(search.search_article_body(connection_string,'test_db','test_collection','body'))) == 1

    assert len(list(search.search_article_body(connection_string,'test_db','test collection','headline'))) == 0

    refresh_test_db()

    



def test_search_headline():
    connection_string = os.environ.get('MONGODB_URL')
    assert len(list(search.search_headline(connection_string,'test_db','test_collection','headline')))  == 0

    test_doc = {'url':'test_url','headline':'test headline','body':'test_body'}

    insert.insert_article(connection_string,'test_db','test_collection',test_doc)

    assert len(list(search.search_headline(connection_string,'test_db','test_collection','headline'))) == 1

    assert len(list(search.search_headline(connection_string,'test_db','test_collection','body'))) == 0

    refresh_test_db()



def test_search():
    connection_string = os.environ.get('MONGODB_URL')
    assert len(list(search.search(connection_string,'test_db','test_collection','test')))  == 0

    test_doc_1 = {'url':'test_url','headline':'test headline doc1','body':'test body'}
    test_doc_2 = {'url':'test_url','headline':'test headline','body':'test body doc2'}

    insert.insert_article(connection_string,'test_db','test_collection',test_doc_1)
    insert.insert_article(connection_string,'test_db','test_collection',test_doc_2)

    assert len(list(search.search(connection_string,'test_db','test_collection','doc1'))) == 1

    assert len(list(search.search(connection_string,'test_db','test_collection','doc2'))) == 1

    assert len(list(search.search(connection_string,'test_db','test_collection','test'))) == 2

    refresh_test_db()