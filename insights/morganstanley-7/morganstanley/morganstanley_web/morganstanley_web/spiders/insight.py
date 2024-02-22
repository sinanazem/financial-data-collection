import json
import re

import scrapy
import w3lib.html

with open('/mnt/c/Users/user/OneDrive/Desktop/morganstanley/morganstanley_web/morganstanley_web/spiders/morganstanley_insights_links.json', 'r') as f:
    json_link = json.load(f)

class InsightSpider(scrapy.Spider):
    name = 'insight'
    allowed_domains = ['www.morganstanley.com']
    start_urls = json_link

    def parse(self, response):
        url = response.url
        content = w3lib.html.remove_tags(response.css('.pageDividerRow').get()).strip()
        content = re.sub('\s+', ' ', content)

        yield {'content':content, 'url':url}
