import scrapy

test_url = "https://emp.jobylon.com/applications/jobs/164268/create/?utm_source=ams&utm_medium=promotionserializer"
# Command:
# scrapy crawl pwspider -o output.json

class PwspiderSpider(scrapy.Spider):
    name = "pwspider"

    def start_requests(self):
        yield scrapy.Request(test_url,
        meta={'playwright': True})

    def parse(self, response):
        yield {
            'text': response.text
        }