import requests
from bs4 import BeautifulSoup
import lxml

from fake_useragent import UserAgent





def pars_rbc():
    URL = 'https://www.rbc.ru/short_news'
    ua = UserAgent().random
    user_agent = {'user_agent': str(ua)}
    GET_URL = requests.get(URL, headers=user_agent)
    soup_even_1 = BeautifulSoup(GET_URL.content, "lxml")
    #g-relative g-clear
    ons = soup_even_1.find('div', class_= 'l-col-container')
    two = ons.find('div', class_ ='l-row js-news-feed-list')
    all_find = two.find_all('div', class_ = 'js-news-feed-item js-yandex-counter', id= True)
    mas = {}

    for i in all_find:

        a = i.find('a', class_ ='item__link rm-cm-item-link js-rm-central-column-item-link')
        string_probel = str(i.text.strip()).replace("\n", '')
        prosto_stroka = string_probel.find('   ')
        c = string_probel[prosto_stroka:].replace('   ', '')
        href_value = a.get('href')
        mas[c] = href_value

    return list(mas.items())[:5]


