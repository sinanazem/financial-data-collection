import scrapy
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import w3lib.html

class InsightSpider(scrapy.Spider):
    name = 'insight'
    allowed_domains = ['www.blackrock.com']
    start_urls = [
                'https://www.blackrock.com/us/individual/insights/paradox-of-crowds',
                'https://www.blackrock.com/us/individual/insights/municipal-monthly',
                'https://www.blackrock.com/us/individual/insights/pricing-power',
                'https://www.blackrock.com/us/individual/insights/unconstrained-fixed-income',
                'https://www.blackrock.com/us/individual/insights/equity-investing-ideas-amid-higher-rates-inflation',
                'https://www.blackrock.com/us/individual/insights/systematic-equity-market-outlook',
                'https://www.blackrock.com/us/individual/insights/retirement/2022-read-on-retirement-survey',
                'https://www.blackrock.com/us/individual/insights/thematic-investing',
                'https://www.blackrock.com/us/individual/insights/value',
                'https://www.blackrock.com/us/individual/insights/blackrock-investment-institute/outlook',
                'https://www.blackrock.com/us/individual/insights/systematic-fixed-income-outlook',
                'https://www.blackrock.com/us/individual/insights/bonds-as-hedge',
                'https://www.blackrock.com/us/individual/insights/blackrock-investment-institute/positioning-for-the-net-zero-transition',
                'https://www.blackrock.com/us/individual/insights/economic-shoulder-season',
                'https://www.blackrock.com/us/individual/insights/taking-stock-quarterly-outlook',
                'https://www.blackrock.com/us/individual/insights/60-40-portfolios-and-alternatives',
                'https://www.blackrock.com/us/individual/insights/growth-stocks',
                'https://www.blackrock.com/us/individual/insights/muni-cef-opportunities',
                'https://www.blackrock.com/us/individual/insights/anna-hawley-on-sustainable-investing',
                'https://www.blackrock.com/us/individual/insights/investing-in-healthcare-stocks',
                'https://www.blackrock.com/us/individual/insights/investing-questions-amid-ukraine-crisis',
                'https://www.blackrock.com/us/individual/insights/gold-still-hedges-chaos',
                'https://www.blackrock.com/us/individual/insights/decoding-the-markets-esg-x-big-data',
                'https://www.blackrock.com/us/individual/insights/prepping-financial-hurricane',
                'https://www.blackrock.com/us/individual/insights/retirement/affording-a-longer-retirement',
                'https://www.blackrock.com/us/individual/insights/bank-loan-cefs',
                'https://www.blackrock.com/us/individual/insights/low-carbon-investing',
                'https://www.blackrock.com/us/individual/insights/garp',
                'https://www.blackrock.com/us/individual/insights/making-sense-uncertainty-markets',
                'https://www.blackrock.com/us/individual/insights/investing-through-longer-and-higher-inflation',
                'https://www.blackrock.com/us/individual/insights/equity-investor-inflation-guide',
                'https://www.blackrock.com/us/individual/insights/blackrock-investment-institute/global-macro-outlook',
                'https://www.blackrock.com/us/individual/insights/international-stock-investing',
                'https://www.blackrock.com/us/individual/insights/retirement/womens-retirement-crisis-podcast',
                'https://www.blackrock.com/us/individual/insights/bonds-as-a-hedge',
                'https://www.blackrock.com/us/individual/insights/valuations',
                'https://www.blackrock.com/us/individual/insights/navigating-market-icebergs',
                'https://www.blackrock.com/us/individual/insights/stakeholder-capitalism-investing',
                'https://www.blackrock.com/us/individual/insights/retirement/2022-retirement-trends',
                'https://www.blackrock.com/us/individual/insights/the-last-hedge-standing',
                'https://www.blackrock.com/us/individual/insights/metaverse-investing-in-the-future',
                'https://www.blackrock.com/us/individual/insights/insight-for-volatile-stock-markets',
                'https://www.blackrock.com/us/individual/insights/equitymarkets',
                'https://www.blackrock.com/us/individual/insights/blackrock-investment-institute/net-zero-transition',
                'https://www.blackrock.com/us/individual/insights/approach-markets-with-perspective',
                'https://www.blackrock.com/us/individual/insights/energy-transition-investing',
                'https://www.blackrock.com/us/individual/insights/quality',
                'https://www.blackrock.com/us/individual/insights/choosing-stocks',
                'https://www.blackrock.com/us/individual/insights/income-outlook-2022',
                'https://www.blackrock.com/us/individual/insights/inflation']

    def parse(self, response):
        content = w3lib.html.remove_tags(response.css('.table-620-wide .row').get()).strip()
        url = response.url
        yield {"content":content, "url":url}


# class InsightSpider(scrapy.Spider):
#     name = 'insight'
#     allowed_domains = ['www.blackrock.com']
#     start_urls = ['https://www.blackrock.com/us/individual/insights']

#     def __init__(self):
#         self.driver = webdriver.Chrome()

#     def parse(self, response):
#         self.driver.get(response.url)

#         titles = response.xpath('//h2/text()').extract()
#         dates = response.xpath('//a//div//div//span[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]/text()').extract()
#         by = response.xpath('//a//div//div//span[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]/text()').extract()
#         descriptions = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "description", " " ))]/text()').extract()

#         links = response.css('.skip-animation ::attr(href)').extract()
#         for title,date,b,description,link in zip(titles,dates,by,descriptions,links):
#             yield {
#                 'title':title.strip(),
#                 'link':link.strip(),
#                 'description':description.strip(),
#                 'date':date.strip(),
#                 'by':b.strip()

#             }
#         button = self.driver.find_element(By.XPATH,'//*[@id="c1561158932259"]/div/div[2]/div/div/div[3]/button')
#         if button:
#             self.driver.execute_script("arguments[0].click();", button)

# class InsightSpider(scrapy.Spider):
#     name = 'insight'
#     allowed_domains = ['www.blackrock.com']
#     start_urls = ['https://www.blackrock.com/us/individual/insights']

#     def parse(self, response):
#         data = json.loads(response.text)
#         yield {"data":data}

