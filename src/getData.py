from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re
import json
import datetime

s = HTMLSession()

def getData(id):
    url = 'https://www.imdb.com/title/' +  id + '/'
    info = {}
    
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    extraHeaders = json.loads(re.findall(r'({.+})', (str(soup.find('script', attrs={ 'type': 'application/json', 'id': '__NEXT_DATA__'}))))[0])
    mainHeader = (extraHeaders['props']['pageProps']['aboveTheFoldData'])
    tsHeader = (extraHeaders['props']['pageProps']['mainColumnData'])
    
    genres = []
    i = 0
    while i < len(mainHeader['genres']['genres']):
        genres.append(mainHeader['genres']['genres'][i]['text'])
        i += 1
    
    if ( mainHeader['titleType']['id'] == 'tvSeries' ):
        try:
            info.update({
                'type' : mainHeader['titleType']['text'],
                'title' : mainHeader['titleText']['text'],      
                'year' : str(mainHeader['releaseYear']['year']) + ' - ' + 'Present' if str(mainHeader['releaseYear']['endYear']) == 'None' else str(mainHeader['releaseYear']['endYear']),           
                'ratings' : mainHeader['ratingsSummary']['aggregateRating'],
                'seasons' : len(tsHeader['episodes']['seasons']),
                'totalepisodes' : tsHeader['episodes']['episodes']['total'],
                'runtime' :  str(datetime.timedelta(seconds=(mainHeader['runtime']['seconds']))),
                'genres' : genres,
                'desc' : mainHeader['primaryVideos']['edges'][0]['node']['description']['value'],
                'poster' : mainHeader['primaryImage']['url'],
                'trailer' : mainHeader['primaryVideos']['edges'][0]['node']['playbackURLs'][0]['url'],
                'cover' : mainHeader['primaryVideos']['edges'][0]['node']['thumbnail']['url']
            })
        except:
            info.update({ 'error' : 'An exception occurred' })
            
    else:
        try:
            info.update({ 
                'type' : mainHeader['titleType']['text'],
                'title' : mainHeader['titleText']['text'],      
                'year' : mainHeader['releaseYear']['year'],           
                'ratings' : mainHeader['ratingsSummary']['aggregateRating'],
                'runtime' :  str(datetime.timedelta(seconds=(mainHeader['runtime']['seconds']))),
                'genres' : genres,
                'desc' : mainHeader['primaryVideos']['edges'][0]['node']['description']['value'],
                'poster' : mainHeader['primaryImage']['url'],
                'trailer' : mainHeader['primaryVideos']['edges'][0]['node']['playbackURLs'][0]['url'],
                'cover' : mainHeader['primaryVideos']['edges'][0]['node']['thumbnail']['url']
                })
        except:
            info.update({ 'error' : 'An exception occurred' })

    return info