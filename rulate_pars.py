

import requests
from bs4 import BeautifulSoup

for count in range(1, 1707):
    url = f'https://tl.rulate.ru/search/index/cat/2/Book_page/{count}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.find('div', class_='span8')
    search_res = data.find('ul', class_='search-results')
    books = search_res.find_all('li', class_='')
    for name in books:
        title = name.find('a').text
        note = name.find('small', class_='cat').text
        all_works = []
        all_works.append(title)
        all_works.append(note)
        desired_works = []
        if 'Английские' in all_works or 'Китайские' in all_works or 'Корейские' in all_works or 'Японские' in all_works:
            desired_works.append(title)
            for work in desired_works:
                print(f'Название:"{title}" | Категория: {note}')
        else:
            pass
