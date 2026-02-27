from requests import Session
from bs4 import BeautifulSoup
import time
import fake_useragent
import urllib3

user = fake_useragent.UserAgent().random

headers = {
    'user-agent': 'user'
}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

work = Session()

work.get('https://quotes.toscrape.com/', headers=headers, verify=False)

response = work.get('https://quotes.toscrape.com/login', headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

token = soup.find('form').find('input').get('value')

data = {
    'csrf_token': token,
    'username': 12345,
    'password': 54321
}

result = work.post('https://quotes.toscrape.com/login',
                   headers=headers, data=data, allow_redirects=True)

for page in range(1, 3):
    link = f'https://quotes.toscrape.com/page/{page}/'
    response = work.get(link, headers=headers, verify=False)
    soup = BeautifulSoup(response.text, 'lxml')

    quotes = soup.find_all('div', class_='quote')
    print(f'Найдено цитат на {page} странице --> {len(quotes)} ')
    print()

    for i, quote in enumerate(quotes, 1):
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = quote.find_all('a', class_='tag')
        tags_list = [teg.text for teg in tags]
        tags_text = ', '.join(tags_list)
        print(f'''{i}) Quote - {text}
    Author - {author}
    Tags: {tags_text}''')
        print()
        time.sleep(1)
