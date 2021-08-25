import scrapy


class Ott21Spider(scrapy.Spider):
    name = 'OTT21'
    allowed_domains = ['12rm.eb.mil.br']
    start_urls = ['https://www.12rm.eb.mil.br/component/phocadownload/category/117.html']

    def parse(self, response):
        for article in response.css("article"):
            link    = article.css("div.texts h2 a::attr(href)").extract_first()
            # title   = article.css("div.texts h2 a::text").extract_first()
            # author  = article.css("div.texts div.info a::text").extract_first()

        yield {'link': link, 'title': title, 'author': author}
