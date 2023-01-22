<br>
<h2 align="center">IMDB Api - V 0.1</h2>

---

<p align="center"> IMDB Scrapper / IMDB API without a key ✨.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](#todo)

## 🧐 About <a name = "about"></a>

Simple python web scrapper to scrape IMDB. <br>
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
- /api/getinfo/{movie_id} - get movie/tv series info
- /api/getimg/{movie_id} - get screenshots of the movie/tv series

<br>{movie_id} is the imdb id of the movie/tv series <br>
You can get the imdb id from the url of the movie/tv series <br>
For example: https://www.imdb.com/title/tt4154796/ <br>
The imdb id is: tt4154796 <br>


## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Kanguage
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Web scrapper
- [FastApi](https://fastapi.tiangolo.com/) - Web framework
- [Uvicorn](https://www.uvicorn.org/) - ASGI Web server

## 📝 Todo <a name = "todo"></a>

- [ ] Add search query endpoint
- [ ] Add top movies endpoint
- [ ] Add trending movies endpoint
- [ ] Create a docker image