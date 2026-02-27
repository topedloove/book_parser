import requests
from bs4 import BeautifulSoup
import urllib3
import time
import fake_useragent

user = fake_useragent.UserAgent().random


headers = {
    'user-agent': user
}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

image_num = 0
storage_number = 1

for storage in range(1):
    link = 'https://zastavok.net'
    response = requests.get(f'{link}/{storage_number}', headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    block = soup.find('div', class_='block-photo')
    all_image = block.find_all('div', class_='short_full')

    for image in all_image:
        image_link = image.find('a').get('href')
        dowload_storage = requests.get(f'{link}{image_link}').text
        dowload_soup = BeautifulSoup(dowload_storage, 'lxml')
        dowload_block = dowload_soup.find(
            'div', class_='image_data').find('div', class_='block_down')
        result_link = dowload_block.find('a').get('href')

        # Dowload image
        image_bytes = requests.get(f'{link}{result_link}').content

        with open(f'image/{image_num}.jpg', 'wb') as file:
            file.write(image_bytes)

        time.sleep(1)
        image_num += 1
        print('Изображение отлично скачено')
    print(f'Картинки скачены с {storage_number} страницы')
    storage_number += 1
