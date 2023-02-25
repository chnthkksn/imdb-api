from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()

url = 'https://www.imdb.com/chart/top'

def getTop():
    list = []
    response = s.get(url)

    soap = BeautifulSoup(response.text, 'html.parser')

    items = soap.find('tbody', attrs={'class': 'lister-list'}).find_all('img')
    rating = soap.find('tbody', attrs={'class': 'lister-list'}).find_all('span', attrs={'name': 'ir'})

    for i in items:
        list.append(
            {
                "no": items.index(i) + 1,
                "title": (i['alt']),
                "img": (i['src']),
                "rating": (rating[items.index(i)]['data-value']),
            }
        )
        
    return list