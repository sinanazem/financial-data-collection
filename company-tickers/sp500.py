import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'wikitable sortable'})
tickers = []

for row in table.find_all('tr')[1:]:
    ticker = row.find_all('td')[0].text.strip()
    name = row.find_all('td')[1].text.strip()
    tickers.append((ticker, name))

pd.DataFrame(tickers, columns=['ticker', 'name'])