from bs4 import BeautifulSoup
import requests
import os
import unicodedata

card_names = []
card_prices = []

os.chdir('E:\\greenfox\\ProjectPhase\\third_week')

links = ['https://www.bestbyte.hu/Videokartya-cVGA.html?p=1',
            'https://www.bestbyte.hu/Videokartya-cVGA.html?p=2',
            'https://www.bestbyte.hu/Videokartya-cVGA.html?p=3',
            'https://www.bestbyte.hu/Videokartya-cVGA.html?p=4',]

for link in links:
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'html.parser')

    for card_n in soup.find_all('div', class_= 'cl_termnev'):
        card_names.append(card_n.text.strip())
    
    for card_p in soup.find_all('div', class_= 'listPrice'):    
        card_prices.append(card_p.text.strip())
        
    print(link + ' is scraped!')

with open('videocard_data.txt', 'w') as f:
    for (name, price) in zip(card_names, card_prices):
        price_edited = price.replace(u'\xa0', '')
        f.write(name + ',' + price_edited + '\n')