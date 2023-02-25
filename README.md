<br>
<h2 align="center">IMDB Api - V 0.1</h2>

---

<p align="center"> IMDB Scraper / IMDB API without a key ✨.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](#todo)

## 🧐 About <a name = "about"></a>

Simple python web scraper to scrape IMDB. <br>
This tool can get the following information:

- Movie Name
- Movie Year
- Movie Rating
- Movie Duration
- Movie Storyline
- Movie Poster
- Movie Trailer

Also it get more info on tv-series :

- Series Episodes
- Series Seasons


## 🚀 Deployment <a name = "deployment"></a>

To deploy this project <br>
clone the project and run the following commands:

```bash
  git clone https://github.com/chnthkksn/imdb-api.git # clone the project
  cd imdb-api # go to project directory
  python -m venv venv # create virtual environment
  venv\Scripts\activate # activate virtual environment
  pip install -r requirements.txt # install requirements
  python main.py # run the project
```

## 🎈 Usage <a name="usage"></a>

After running the project you can use the following endpoints: <br>

- /docs - all the endpoints and their usage
- /api/search/{query} - search for a movie/tv series by name ( urlencode the query - ex: /api/search/avengers%20endgame )
- /api/getinfo/{movie_id} - get movie/tv series info
- /api/getimg/{movie_id} - get screenshots of the movie/tv series
- /api/akas/{movie_id} - get as known as titles of the movie/tv series
- /api/topmovies - get top 250 movies

<br>{movie_id} is the imdb id of the movie/tv series <br>
You can get the imdb id from the url of the movie/tv series <br>
For example: https://www.imdb.com/title/tt4154796/ <br>
The imdb id is: tt4154796 <br>


## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 
- [FastApi](https://fastapi.tiangolo.com/) 
- [Uvicorn](https://www.uvicorn.org/) 

## 📝 Todo <a name = "todo"></a>

- [x] Add search query endpoint
- [x] Add top movies endpoint
- [ ] Add trending movies endpoint
- [ ] Create a docker image
- [x] Add as known as titles endpoint