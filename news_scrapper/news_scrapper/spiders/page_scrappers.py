import json
    
# module that contains the methods to process various types of pages on bbc website
class PageScrapper():
    
    # parse the bbc news pages.
    def parse_news_page(self,response):
        url = response.request.url
        
        data = {
                "url": url, 
                "headline": response.css('[id="main-heading"]::text').get(),
                "body": [paragraph[1].xpath('div/p/text()').get() for paragraph in enumerate(response.xpath('//div[@data-component="text-block"]')) ]  
               }
        
        yield {'url': url}
    

    # parse the bbc article pages.
    def parse_article_page(self,response):
        url = response.request.url

        article_body = response.xpath('//article')

        data = {
                "url": url, 
                "headline": response.css('[class="article-headline__text b-reith-sans-font b-font-weight-300"]::text').get(),
                "body": [paragraph[1].xpath('text()').get() for paragraph in enumerate(article_body.xpath('//p'))]
                }
        
        yield {'url': url}
        