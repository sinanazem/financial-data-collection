import scrapy
import w3lib.html

import re

class InsightSpider(scrapy.Spider):
    name = 'insight'
    allowed_domains = ['www.blackrock.com']
    start_urls = ['https://www.blackrock.com/institutions/en-us/insights']

    def parse(self, response):
        title_list = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "full-width", " " ))]//h2/text()').extract()
        abstract_list = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "skip-animation", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "description", " " ))]/text()').extract()
        date_list = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "date", " " ))]').extract()
        link_list = response.xpath("//*[@class='cta link article-wrapper-link skip-animation']/@href").extract()
        tag_list = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "category", " " ))]').extract()

        for title, abstract, date, link, tag in zip(title_list, abstract_list, date_list, link_list, tag_list):

            yield {
                "title": title.strip() ,
                "tag": re.sub('\s+', ' ', w3lib.html.replace_tags(tag).strip()),
                "date": re.sub('\s+', ' ', w3lib.html.replace_tags(date).strip()),
                "link": f"https://www.blackrock.com{link}",
                "abstract": abstract.strip(),
            }
