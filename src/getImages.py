from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json
import re

s = HTMLSession()

def getImages(id, limit):
    url = 'https://www.imdb.com/title/' +  id + '/'
    images = []
    mediaUrl = url + 'mediaindex'
    limit = 5 if limit == None or limit == 0 else limit
    
    r = s.get(mediaUrl)
    soup = BeautifulSoup(r.text, 'html.parser')
    imageList = soup.find('div', attrs='media_index_thumb_list').select('a')
    
    limit = len(imageList) if len(imageList) < limit else limit
    
    x = 0
    while x < limit:
        if limit - x == 1:
            imgLink = 'https://www.imdb.com/' + imageList[x]['href']
            imgId = re.findall(r'(rm[a-z0-9]+)', imgLink)
            r = s.get(imgLink)
            soup = BeautifulSoup(r.text, 'html.parser')
            img = soup.find('img', attrs={'data-image-id': imgId[0] + '-curr'})
            try:
                images.append(img['src'])
            except:
                pass            
            x += 1
            
        elif limit - x == 2:
            imgLink = 'https://www.imdb.com/' + imageList[x+1]['href']
            r = s.get(imgLink)
            soup = BeautifulSoup(r.text, 'html.parser')
            imgId = re.findall(r'data-image-id=\"(rm[a-z0-9]+)', str(soup))
            try:
                images.append( soup.find('img', attrs={'data-image-id': imgId[0] + '-prev'})['src'] )
                images.append( soup.find('img', attrs={'data-image-id': imgId[1] + '-curr'})['src'] )
            except:
                pass
            x += 2
            
        else:
            imgLink = 'https://www.imdb.com/' + imageList[x+1]['href']
            r = s.get(imgLink)
            soup = BeautifulSoup(r.text, 'html.parser')
            imgId = re.findall(r'data-image-id=\"(rm[a-z0-9]+)', str(soup))
            try:
                images.append( soup.find('img', attrs={'data-image-id': imgId[0] + '-prev'})['src'] )
                images.append( soup.find('img', attrs={'data-image-id': imgId[1] + '-curr'})['src'] )
                images.append( soup.find('img', attrs={'data-image-id': imgId[2] + '-prev'})['src'] )
            except:
                pass
            x += 3
            
        
    return images
    
    