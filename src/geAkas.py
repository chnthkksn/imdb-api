import requests
from requests_html import HTMLSession
import json as json
from bs4 import BeautifulSoup
import re

s = HTMLSession()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
    'Accept': 'application/graphql+json, application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.imdb.com/',
    'content-type': 'application/json',
    'x-imdb-client-name': 'imdb-web-next-localized',
    'x-imdb-user-language': 'en-US',
    'x-imdb-user-country': 'US',
    'x-imdb-weblab-treatment-overrides': '{"IMDB_DESKTOP_SEARCH_ALGORITHM_UPDATES_577300":"T1"}',
    'Origin': 'https://www.imdb.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
}

def getAkas(id):
    
    url = 'https://www.imdb.com/title/'+ id +'/releaseinfo/'
    akas = []
    
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    extraHeaders = json.loads(re.findall(r'({.+})', (str(soup.find('script', attrs={ 'type': 'application/json', 'id': '__NEXT_DATA__'}))))[0])
      
    akaData = extraHeaders["props"]["pageProps"]["contentData"]["categories"][1]["section"]["items"]
    
    for i in akaData:
        akas.append(
            {
                "country": i["rowTitle"] if "rowTitle" in i else i["listContent"][0]["subText"],
                "title": i["listContent"][0]["text"]
            }
        )
    
    params = {
    'operationName': 'TitleAkasPaginated',
    'variables': '{"after":"NA==","const":"id","first":50,"locale":"en-US","originalTitleText":false}',
    'extensions': '{"persistedQuery":{"sha256Hash":"180f0f5df1b03c9ee78b1f410d65928ec22e7aca590e5321fbb6a6c39b802695","version":1}}',
    }
    
    params["variables"] = params["variables"].replace("id", id)
    
    response = requests.get('https://caching.graphql.imdb.com/', params=params, headers=headers)

    response = json.loads(response.text)
    response = response["data"]["title"]["akas"]["edges"]
    
    for i in response:
        akas.append(
            {
                "country": i["node"]["country"]["text"],
                "title": i["node"]["displayableProperty"]["value"]["plainText"],
            }
        )
        
    return akas