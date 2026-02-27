import requests
from bs4 import BeautifulSoup
import fake_useragent
import urllib3
import time

user = fake_useragent.UserAgent().random
header = {
    'user-agent': user
}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

for page in range(1, 11):
    link = f'https://quotes.toscrape.com/page/{page}/'
    response = requests.get(link, headers=header, verify=False)
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
