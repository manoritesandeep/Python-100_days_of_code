from bs4 import BeautifulSoup
import requests

# URL = "https://www.empireonline.com/movies/features/best-movies-2/"
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
website_html = response.text
# print(website_html)

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())
# <h3 class="jsx-4245974604">100) Reservoir Dogs</h3>
movie_names = soup.find_all(name="h3", class_="title")
# print(movie_names)
movie_title = [movie.getText() for movie in movie_names]
# print(movie_title[::-1])
# print(movie_title[0].strip().split(")")[1])
# for n in range(len(movie_title) - 1, -1, -1):
#     print(movie_title[n])
movies = movie_title[::-1]
# print(movies)

# write to text file
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
