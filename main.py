import requests
from bs4 import BeautifulSoup

data = requests.get(YOUR_URL) #I have used this url https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/

soup = BeautifulSoup(data.text, "html.parser")
print(soup.prettify())
movie_name = soup.find_all(name="h3", class_="title")
# print(soup)
print(movie_name)
movies = []
for i in movie_name:
    movies.append(i.get_text())
movies.reverse()
print(movies)
for k in movies:
    with open(file="movie.txt", mode="a", encoding="utf-8") as file:

        file.write(f"{k}\n")
        print(k)
