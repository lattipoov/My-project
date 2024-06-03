import requests
from bs4 import BeautifulSoup

def aloqabank():
    FQDN = 'https://aloqabank.uz/ru/'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }
    html = requests.get(FQDN, headers=HEADERS).text
    soup = BeautifulSoup(html, 'html.parser')
    block = soup.find('table', class_='exchange__table')
    all_tr = block.find_all('tr')
    value = []
    for tr in all_tr:
        exchange_value = tr.find_all('div', class_='exchange-value')
        if len(exchange_value) > 2:
            value.append(exchange_value[0].find('span').get_text())
            value.append(exchange_value[1].find('span').get_text())
            value.append(exchange_value[2].find('span').get_text())
            break

    return tuple(value)



aloqabank()