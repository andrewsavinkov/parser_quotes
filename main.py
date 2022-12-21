import requests
from bs4 import BeautifulSoup as bs
from random import randint

def random_quote():
    url='https://finewords.ru/'
    response=requests.get(url).text
    soup=bs(response, 'html.parser')
    citate = soup.find_all('div', class_='cit')[randint(0, 249)].find('p').text
    print(citate)

random_quote()
