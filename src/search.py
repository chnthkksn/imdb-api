from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json
import unicodedata

s = HTMLSession()

def search(q):
    url = f"https://www.imdb.com/find/?s=tt&q={q}"
    results = []
    
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
   
    list = soup.find('script', attrs={'id':"__NEXT_DATA__",'type':"application/json"})
    movies = json.loads(list.text)['props']['pageProps']['titleResults']['results']
    
    for movie in movies:
        results.append({
            'id' : movie['id'],
            'name' : movie['titleNameText'],
            'year' : unicodedata.normalize("NFKD", movie['titleReleaseText']) if movie.get('titleReleaseText') else None,
            'credits' : movie['topCredits'] if movie.get('topCredits') else None,
            'image' : movie['titlePosterImageModel']['url'] if movie.get('titlePosterImageModel') else None,
            'type' : movie['imageType']
        })
    
    
    return(results)