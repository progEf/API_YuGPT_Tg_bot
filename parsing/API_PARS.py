import requests
from bs4 import BeautifulSoup
import lxml

from fake_useragent import UserAgent

from parsing.parsing_RBK import pars_rbc






def request_parsing(st):
    endpoint = 'https://300.ya.ru/api/sharing-url'
    response = requests.post(
        endpoint,
        json={
            'article_url': st
        }, headers={'Authorization': 'OAuth y0_AgAAAABfE_mwAAoX4wAAAADmh-TsrwqldS4UR0q5quwqrNM2-KTuRTk'})
    print(response.json())
    URL = response.json()['sharing_url']
    ua = UserAgent().random
    user_agent = {'user_agent': str(ua)}
    GET_URL = requests.get(URL, headers=user_agent)
    soup_even_1 = BeautifulSoup(GET_URL.content, "lxml")
    one = soup_even_1.find('div', class_ = 'container')
    two = one.find('div', class_ = 'content-theses svelte-h3ittf')
    three =two.find('ul', class_ = 'svelte-h3ittf')
    tho = three.find_all('li', class_= 'svelte-h3ittf')
    mas = []
    for i in tho:
        mas.append(i.text)
    return mas

#for i in pars_rbc():
#    print(i)
#
#for c in pars_rbc():
#    if c[0] == 'В Петербурге мужчина выстрелил в девушку и покончил с собой':
#        print(c[1])

