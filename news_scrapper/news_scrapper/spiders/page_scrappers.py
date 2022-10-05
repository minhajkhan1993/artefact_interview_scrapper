import json
from mongodb.mongodb import MongoDB
import mongodb.insert as insertModule
import os
    
# module that contains the methods to process various types of pages on bbc website
class PageScrapper():
    
    # inserts page objects into mongodb database
    def insert_page(self,page_data):
        
        # submit page to be inserted to mongodb's insert module
        result = insertModule.insert_article(os.environ.get('MONGODB_URL'), os.environ.get('Mongo_Database'), os.environ.get('Mongo_Collection'), page_data)
        return result
    

    # build the object that will be stored in database
    def make_article_object(self, url: str, headline: str, body: str) -> dict:
        
        data = {
                "url": url, 
                "headline": headline,
                "body": body
                }
        
        return data
    
    
    # parse the bbc news pages.
    def parse_news_page(self,response):
        url = response.request.url
    
        page_body_content = []
        
        # search for divs within the article body that contain article text.
        for paragraph in enumerate(response.xpath('//div[@data-component="text-block"]')):
            
            # extract text from <p> or <b> tags
            bold_div_content = paragraph[1].xpath('div/p//b/text()').get()
            para_div_content = paragraph[1].xpath('div/p/text()').get()

            if not bold_div_content is None:
                page_body_content.append(bold_div_content)
            
            if not para_div_content is None:
                page_body_content.append(para_div_content)  
        
        
        # extract headline from page
        headline = response.css('[id="main-heading"]::text').get()
        
        # build the object that will be stored in database
        data = self.make_article_object(url, headline, page_body_content)
        
        self.insert_page(data)
    
        yield {'url': url}
    

    # parse the bbc article pages.
    def parse_article_page(self,response):
        url = response.request.url

        page_body_content = []
        
        # search for tags within the article body that contain article text.
        article_body = response.css('[class="article"]')
        for paragraph in enumerate(article_body.xpath('//p')):
            
            # extract text from <p> tags found. 
            div_content = paragraph[1].xpath('text()').get()
            
            if not div_content is None:
                page_body_content.append(div_content)


        # extract headline from page
        headline = response.css('[class="article-headline__text b-reith-sans-font b-font-weight-300"]::text').get()       
        
        # build the object that will be stored in database
        data = self.make_article_object(url, headline, page_body_content)
        
        self.insert_page(data)
        
        yield {'url': url}
    

    # parse the bbc audio/visual reports pages.
    def parse_av_page(self,response):
        url = response.request.url
    
        page_body_content = []
        
         # search for tags within the article body that contain article text.
        for paragraph in enumerate((response.css('[class="ssrcss-1s1kjo7-RichTextContainer e5tfeyi1"]')).xpath('p')):
            para_div_content = paragraph[1].xpath('text()').get()
            
            if not para_div_content is None:
                page_body_content.append(para_div_content)  
        

        # extract headline from page
        headline = response.css('[id="main-heading"]::text').get()

        # build the object that will be stored in database
        data = self.make_article_object(url, headline, page_body_content)
        
        self.insert_page(data)
    
        yield {'url': url}