from curses import REPORT_MOUSE_POSITION
from subprocess import call
import scrapy
import re
from .page_scrappers import PageScrapper


class QuotesSpider(scrapy.Spider):
    name = "news"

    # top level request processing function that is called by scrapy.
    def start_requests(self):  
        return self.process_requests('https://www.bbc.com/news',0)

    
    # callback for start_requests.
    # url is the url to be processed. level is the depth at which the current url was discovered
    def process_requests(self, url, level):
        yield scrapy.Request(url=url, callback=self.parse_links, cb_kwargs=dict(level=level))

    
    # callback for process_requests
    # processes hyperlinks from the the current page
    def parse_links(self, response, level):
        
        # new instance of page scrapper module
        page_scrapper = PageScrapper()
        
        if level < 2:             
            # iterate over hyperlinks found on the page
            for hyperlink in response.xpath('//a'):
                url = hyperlink.xpath('./@href').get()
                
                # check if url has format "/news/...{7 digit id starting with 6}". These are bbc news reports
                if re.search("\/news\/.*6\d{7}", url):
                    if not re.search('bbc.co',url):
                        url = 'https://www.bbc.com' + url
                    yield scrapy.Request(url=url, callback=page_scrapper.parse_news_page) 
                
                # check if url has format ".../article/...". These are bbc op-ed articles
                elif re.search("article", url):
                    if not re.search('bbc.co',url):
                        url = 'https://www.bbc.com' + url
                    yield scrapy.Request(url=url, callback=page_scrapper.parse_article_page)
                
                # parse all other pages for more news and articles pages
                elif re.search('bbc.com',url):
                    yield scrapy.Request(url=url, callback=self.parse_links, cb_kwargs=dict(level=level+1))


    