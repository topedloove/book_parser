import requests
from bs4 import BeautifulSoup
import fake_useragent
import urllib3
import time
import json

user = fake_useragent.UserAgent().random

headers = {
    'user-agent': user
}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

link = 'https://books.toscrape.com/index.html'

response = requests.get(link, headers=headers, verify=False).text

soup = BeautifulSoup(response, 'lxml')

all_book_cards = soup.find('ol', class_='row').find_all(
    'li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

data_card = []
count_card = 1
count_all_card = int(len(all_book_cards))

for book_card in all_book_cards:
    print(f'Обработка карточки №{count_card}')
    link_book_card = 'https://books.toscrape.com/' + \
        book_card.find('div', class_='image_container').find('a').get('href')
    response_book_card = requests.get(
        link_book_card, headers=headers, verify=False, timeout=10).text
    soup_book_card = BeautifulSoup(response_book_card, 'lxml')

    try:
        name_book = soup_book_card.find(
            'div', class_='col-sm-6 product_main').find('h1').text
        print(f'Объект успешно  найден!')
    except Exception:
        print(f'Объект не найден')

    try:
        price_book = soup_book_card.find(
            'div', class_='col-sm-6 product_main').find('p', class_='price_color').text
        print(f'Объект успешно  найден!')
    except Exception:
        print(f'Объект не найден')

    try:
        in_stock = soup_book_card.find(
            'p', class_='instock availability').text.strip()
        print(f'Объект успешно найден!')
    except Exception:
        print(f'Объект не найден')

    try:
        book_warning = soup_book_card.find(
            'div', class_='alert alert-warning').text
        print('Объект успешно найден')
    except Exception:
        print(f'Объект не найден')

    data_card.append(
        {
            'Name book:': name_book,
            'Price book:': price_book,
            'In stock:': in_stock,
            'book warning: ': book_warning
        }
    )
    print(f'Обработка карточки №{count_card} завершена')
    print(
        f'Обработано карточек - {count_card}, осталось - {count_all_card-count_card}')
    count_card += 1
    time.sleep(2)

with open('myenv/data_cards.json', 'w', encoding='utf-8') as file:
    json.dump(data_card, file, indent=4, ensure_ascii=False)

print('Поздравляю! Обработка полностью завершена.')
