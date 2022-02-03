import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

# Scraping all the titles
titles = soup.find_all(name='h3', class_='title')
titles = [title.get_text() for title in titles]
titles.reverse()


#Writing to txt file
with open('movies.txt', 'w', encoding="utf8") as file:
   for title in titles:
        file.write(title)
        file.write('\n')




