import requests
from mongodb.mongodb import MongoDB
import os
import mongodb.insert as insert




def test_search_by_keyword():
    response = requests.get('http://127.0.0.1:8000/search/xvy')

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["search_result"] == []

    connection_string = os.environ.get('MONGODB_URL')

    test_doc_1 = {'url':'test_url_1','headline':'test headline doc1','body':'test body'}
    test_doc_2 = {'url':'test_url_2','headline':'test headline','body':'test body doc2'}

    insert.insert_article(connection_string, os.environ.get('Mongo_Database'),os.environ.get('MONGO_COLLECTION'),test_doc_1)
    insert.insert_article(connection_string,os.environ.get('Mongo_Database'),os.environ.get('MONGO_COLLECTION'),test_doc_2)

    response = requests.get('http://127.0.0.1:8000/search/doc1')

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["search_result"][0]['url'] == 'test_url_1'


    response = requests.get('http://127.0.0.1:8000/search/doc2')

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["search_result"][0]['url'] == 'test_url_2'


    response = requests.get('http://127.0.0.1:8000/search/test')

    assert response.status_code == 200

    response_body = response.json()

    assert len(response_body["search_result"]) > 1




def test_search_headline_by_keyword():
    response = requests.get('http://127.0.0.1:8000/search/headline/xvy')

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["search_result"] == []

    connection_string = os.environ.get('MONGODB_URL')

    test_doc = {'url':'test_url_1','headline':'api_test_headline','body':'api_test_body'}

    insert.insert_article(connection_string, os.environ.get('Mongo_Database'),os.environ.get('MONGO_COLLECTION'),test_doc)

    response = requests.get('http://127.0.0.1:8000/search/headline/api_test_headline')

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["search_result"][0]['url'] == 'test_url_1'


    response = requests.get('http://127.0.0.1:8000/search/headline/api_test_body')

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["search_result"] == []





def test_search_article_body_by_keyword():
    response = requests.get('http://127.0.0.1:8000/search/article_body/xvy')

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["search_result"] == []

    connection_string = os.environ.get('MONGODB_URL')

    test_doc = {'url':'test_url_1','headline':'api_test_headline','body':'api_test_body'}

    insert.insert_article(connection_string, os.environ.get('Mongo_Database'),os.environ.get('MONGO_COLLECTION'),test_doc)

    response = requests.get('http://127.0.0.1:8000/search/article_body/api_test_body')

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["search_result"][0]['url'] == 'test_url_1'


    response = requests.get('http://127.0.0.1:8000/search/article_body/api_test_headline')

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["search_result"] == []