import scrapy


class InsightSpider(scrapy.Spider):
    name = 'insight'
    allowed_domains = ['www.ubs.com']
    start_urls = [
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/house-view/2022/weekly-deep-dive.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2022/sustainable-investing-perspectives.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/house-view/2022/monthly.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/2020/bear-market-guidebook.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/de/en/wealth-management/our-service/private-equity.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/2022/women-and-investing-reimagining-wealth-advice.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/wealth-planning/executives-and-entrepreneurs/2019/pre-sale-of-your-business.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/wealth-planning/executives-and-entrepreneurs/2019/during-the-sale-of-your-business.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/wealth-planning/executives-and-entrepreneurs/2019/how-to-sell-your-business.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/wealth-planning/executives-and-entrepreneurs/2019/post-sale-of-your-business.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2021/us-china-tensions.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/wealth-planning/executives-and-entrepreneurs/2019/how-to-invest-lump-sum.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2021/the-global-engine-of-new-mobility.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2020/tech-disruption-asean-economy.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/wealth-planning/executives-and-entrepreneurs/2021/commercial-case-diversity-and-inclusion.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/global-risk-radar/2021/february.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2020/three-steps-to-sustainable-and-profitable-business.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2020/asia-recovering-from-covid19.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2020/private-investors.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2020/is-india-the-new-china.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/wealth-planning/executives-and-entrepreneurs/2020/doing-business-in-europe-opportunities.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2020/asia-esg-investing.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/wealth-planning/executives-and-entrepreneurs/2020/industry-4-point-zero-after-covid-19.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2020/covid19-impact-asean-economy.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2020/dcep-chinas-digital-currency.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2020/truths-about-sustainable-investing.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2020/six-impact-investment-opportunities.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2020/how-5g-empowers-different-industries.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2020/china-5g-opportunity.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/2019/decade-ahead-game.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/2019/year-ahead.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2019/food-revolution.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/wealth-planning/executives-and-entrepreneurs/2019/diversify-investments-as-business-owners.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2019/future-of-europe.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2019/shifting-asia-hub.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/2019/quantitative-tightening-impact.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2019/wef-2019.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2018/china-biotech.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2018/investing-in-china-dragon-awakens.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2018/7-ways-of-investing.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2017/interview-chuck-slaughter-living-goods.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2017/interview-david-hertz-gastromotiva.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2018/five-lessons-on-sustainability-un-sdg-wef.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/2017/sustainability-challenges.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2017/corporate-health.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2017/sustainable-impact-investing.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2017/wef-white-paper-2017.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2017/business-with-impact.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2017/africa-cradle-of-diversity.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2017/trump-100-days.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2017/gender-lens-wealth.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2017/prosperity-beyond-oil.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2017/un-sustainable-development-goals.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2017/impact-investing-needs-siliconvalley.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2017/why-sustainable-investing-is-a-game-changer-investors.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2017/which-sdgs-should-private-wealth-focus-on-fulfilling.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2017/breaking-down-barriers-private-wealth-fund-sdgs.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2017/recommendations-private-investors-public-good.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/regional-outlook/2017/trade-war-affect-global-markets.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/sustainable-investing/2017/five-percent-returns.html?caasID=CAAS-ActivityStream',
                'https://www.ubs.com/global/en/wealth-management/insights/insights-display-adp/global/en/wealth-management/insights/chief-investment-office/market-insights/2017/the-end-game.html?caasID=CAAS-ActivityStream']

    def parse(self, response):
        content = response.


driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)
driver.execute_script("arguments[0].click();", button)