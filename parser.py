import random
import requests
from bs4 import BeautifulSoup

url = 'https://more-novinok.org/poslednie-filmy/'

responceWebParser = requests.get(url)
data = BeautifulSoup(responceWebParser.text, 'html.parser')
dataFilms = {}

def get_film():
    for film_data in data.find_all('div', class_='poster grid-item has-overlay js-show-info'):
        name_film = film_data.div.img['alt'][9:]
        link = film_data.h3.a['href']
        dataFilms[name_film] = link
    rKey = random.choice(list(dataFilms.keys()))
    return f'Название фильма:\n{rKey}\n\nСсылка на фильм:\n{dataFilms[rKey]}'