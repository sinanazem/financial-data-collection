import re
from concurrent.futures import process
from datetime import datetime
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import scrapy
import w3lib.html
from scrapy.crawler import CrawlerProcess

def extract_tag_content(link):
    try:

        response = requests.get(link)

        #response = requests.get(link)
        soup = BeautifulSoup(response.text, 'lxml')

        content = soup.findAll("div",class_='paragraph tinymce clearfix bg-white table-620-wide')
        if bool(content) is True:
            content = " ".join([i.text for i in soup.findAll("div",class_='paragraph tinymce clearfix bg-white table-620-wide')])
            content = re.sub('\s+',' ',content)

        else:
            content = 'N/A'

        return content

    except:
        print(f'link must be fix!:{link}')


def blackrock_date(date):

    format_1 = re.findall(r"\b\w+\s\d+,\s\d+\b",date)
    format_2 = re.findall(r"\b\d+/\d+/\d+\b",date)

    if bool(format_1) is True:
        date = datetime.strptime(''.join(format_1), "%b %d, %Y").date()
        return str(date)
    elif bool(format_2) is True:
        date = datetime.strptime(''.join(format_2), "%m/%d/%Y").date()
        return str(date)

class BlackSpider(scrapy.Spider):
    name = 'Black'

    def start_requests(self):
        yield scrapy.Request('https://www.blackrock.com/institutions/en-us/insights')

    def parse(self, response, **kwargs):

        title_list = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "full-width", " " ))]//h2/text()').extract()
        abstract_list = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "skip-animation", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "description", " " ))]/text()').extract()
        date_list = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "date", " " ))]').extract()
        link_list = response.xpath("//*[@class='cta link article-wrapper-link skip-animation']/@href").extract()
        tag_list = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "category", " " ))]').extract()
        index = 0
        for title, abstract, date, link, tag in zip(title_list, abstract_list, date_list, link_list, tag_list):
            index += 1
            yield {
                "index": index,
                "company": "BlackRock",
                "topic": "Institutional insights",
                "tag": re.sub('\s+', ' ', w3lib.html.replace_tags(tag).strip()),
                "section": "",
                "title": title.strip(),
                "date": blackrock_date(re.sub('\s+', ' ', w3lib.html.replace_tags(date).strip())),
                "link": urljoin("https://www.blackrock.com",link),
                "abstract": abstract.strip(),
                "content": extract_tag_content(urljoin("https://www.blackrock.com",link))
            }



if __name__ == "__main__":

    process = CrawlerProcess(settings={
        'FEEDS': {
            './blackrock_institutional_insights_without_content.json': {'format': 'json'},
        }
    })

    process.crawl(BlackSpider)
    process.start()
