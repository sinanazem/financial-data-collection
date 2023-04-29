from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
import re
import time

class EarningsCallsLinks:
    def __init__(self, url, start_date=None):
        
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        self.driver.find_element(By.ID,'onetrust-accept-btn-handler').click()
        time.sleep(5)
        if self.driver.find_elements(By.XPATH,'//*[@id="modal-form"]/fieldset/ul[1]/li[1]/label/input'):
            self.driver.find_element(By.XPATH,'//*[@id="modal-form"]/fieldset/ul[1]/li[1]/label/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="modal-form"]/fieldset/ul[2]/li[1]/label/input').click()
            self.driver.find_element(By.XPATH,'//*[@id="gdpr-submit-button"]').click()

    def get_transcripts_links(self):

        

        while True:
            try:
                button = self.driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div[1]/section[2]/div/div/div[1]/div/div/button")
                self.driver.execute_script("arguments[0].click();", button)
                pattern = re.compile("(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2},\s+\d{4}")
                
                last_t_page = self.driver.find_element(By.XPATH,"(//*[@class='text-gray-1100'])[last()]").text
                date = pattern.search(last_t_page)
                if datetime.strptime(date.group(), "%B %d, %Y") < datetime.strptime('2022-01-01', "%Y-%m-%d"):
                    break
            except: 
                break

        time.sleep(5)

        list_of_article = self.driver.find_elements(By.XPATH, "//a[@class='text-gray-1100']")
        links_list = [link.get_attribute('href') for link in list_of_article]
        
        return links_list
    
    
if __name__ == "__main__":
    obj = EarningsCallsLinks("https://www.fool.com/earnings-call-transcripts/")
    obj.get_transcripts_links()