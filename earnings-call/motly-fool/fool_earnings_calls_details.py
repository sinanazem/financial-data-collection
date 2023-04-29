from datetime import datetime

import requests
from bs4 import BeautifulSoup


def get_transcripts_detailes(url):
    response = requests.get(url)
    if response.ok:
        
        soup = BeautifulSoup(response.text)
    else: 
        raise Exception(f'response is {response}')
    
    try:
        title = soup.find('h1', {'class': 'font-medium'}).text
    except:
        title = ''
    try:
        ticker = soup.find('a', {'class': 'ticker-symbol'}).text
    except:
        ticker = ''
    try:
        content = soup.find('div', {'class': 'tailwind-article-body'}).text
    except:
        content
    try:
        date = soup.find('span', {'id': 'date'}).text
    except:
        date = ''
    try:
        market_cap = soup.find('div', {'class': 'font-bold text-right text-gray-1100'}).text
    except:
        market_cap = ''
    try:
        today_change = soup.find('div', {'class': 'w-full text-lg font-medium bg-red-200 p-8px text-gray-1100'}).text
    except:
        today_change = ''
    try:
        current_price = soup.find('div', {'class': 'text-sm font-medium lg:text-right lg:pl-8px text-gray-1100 p-8px lg:text-lg'}).text
    except:
        current_price = ''
    
    detail_transcripts_dict = {
        'ticker': ticker,
        'title': title,
        'date': date,
        'crawled_date':datetime.today(),
        'market_cap': market_cap,
        'current_price': current_price,
        'today_change': today_change,
        'link':url,
        'content': content,
    }
    return detail_transcripts_dict


if __name__ == "__main__":
    dict_ = get_transcripts_detailes('https://www.fool.com/earnings/call-transcripts/2023/02/09/xpo-xpo-q4-2022-earnings-call-transcript/')
    print(dict_)
    