import requests
from bs4 import BeautifulSoup
import urllib3
import fake_useragent
import time

user = fake_useragent.UserAgent().random

headers = {
    'user-agent':  user
}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


link = 'https://www.wowpaper.net/ru'

response = requests.get(link, headers=headers, verify=False).text

soup = BeautifulSoup(response, 'lxml')


image_category = soup.find(
    'ul', class_='images-grid').find_all('li', class_='images-grid__item')

image_num = 0

for category in image_category:
    category_link = category.find('a').get('href')
    time.sleep(1.5)
    response_category = requests.get(
        category_link, headers=headers, verify=False).text
    response_category_soup = BeautifulSoup(response_category, 'lxml')
    all_image_category = response_category_soup.find(
        'ul', class_='images-grid').find_all('li', class_='images-grid__item')
    print(category_link)
    for image in all_image_category:
        image_link = image.find('a').get('href')
        time.sleep(1.5)
        response_image_link = requests.get(
            image_link, headers=headers, verify=False).text
        response_image_link_soup = BeautifulSoup(response_image_link, 'lxml')
        dowload_link = response_image_link_soup.find(
            'div', class_='wall-picture__buttons').find('a').get('href')
        # Download image
        image_bytes = requests.get(dowload_link).content
        with open(f'image/{image_num}.jpg', 'wb') as file:
            file.write(image_bytes)
        image_num += 1
        print('Изображение скачено!')
    time.sleep(1.5)
