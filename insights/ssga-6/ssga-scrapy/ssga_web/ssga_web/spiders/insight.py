import scrapy


class InsightSpider(scrapy.Spider):
    name = 'insight'
    allowed_domains = ['www.ssga.com']
    start_urls = ['https://www.ssga.com/us/en/intermediary/ic/insights?g=strategies:active-quantitative-equity-aqe']

    def parse(self, response):
        content = response.css('.aem-GridColumn--default--9 .item ::text').extract()
        for i in content:
            yield {"content": i,
                "url": response.url}
