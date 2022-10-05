import json
from mongodb.mongodb import MongoDB
import mongodb.insert as insertModule
import os
    
# module that contains the methods to process various types of pages on bbc website
class PageScrapper():
    
    def insert_page(self,page_data):
        mongo_instance = MongoDB()
        mongo_instance.createMongoClient(os.environ.get('MONGODB_URL'))

        result = insertModule.insert_article(mongo_instance, os.environ.get('Mongo_Database'), os.environ.get('Mongo_Collection'), page_data)
        return result
    
    
    
    # parse the bbc news pages.
    def parse_news_page(self,response):
        url = response.request.url
    
        page_body_content = []
        
        for paragraph in enumerate(response.xpath('//div[@data-component="text-block"]')):
            bold_div_content = paragraph[1].xpath('div/p//b/text()').get()
            para_div_content = paragraph[1].xpath('div/p/text()').get()

            if not bold_div_content is None:
                page_body_content.append(bold_div_content)
            
            if not para_div_content is None:
                page_body_content.append(para_div_content)  
        
        data = {
                "url": url, 
                "headline": response.css('[id="main-heading"]::text').get(),
                "body": page_body_content  
               }
        
        self.insert_page(data)
    
        yield {'url': url}
    

    # parse the bbc article pages.
    def parse_article_page(self,response):
        url = response.request.url

        page_body_content = []
        
        article_body = response.css('[class="article"]')
        for paragraph in enumerate(article_body.xpath('//p')):
            div_content = paragraph[1].xpath('text()').get()
            if not div_content is None:
                page_body_content.append(div_content)

        data = {
                "url": url, 
                "headline": response.css('[class="article-headline__text b-reith-sans-font b-font-weight-300"]::text').get(),
                "body": page_body_content
                }
        
        self.insert_page(data)
        
        yield {'url': url}
    

    # parse the bbc news pages.
    def parse_av_page(self,response):
        url = response.request.url
    
        page_body_content = []
        
        for paragraph in enumerate((response.css('[class="ssrcss-1s1kjo7-RichTextContainer e5tfeyi1"]')).xpath('p')):
            para_div_content = paragraph[1].xpath('text()').get()
            
            if not para_div_content is None:
                page_body_content.append(para_div_content)  
        
        data = {
                "url": url, 
                "headline": response.css('[id="main-heading"]::text').get(),
                "body": page_body_content  
               }
        
        self.insert_page(data)
    
        yield {'url': url}