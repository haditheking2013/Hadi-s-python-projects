from bs4 import BeautifulSoup
import requests


response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
contents = response.text
soup = BeautifulSoup(contents)
print(soup.title.get_text(),'html.parser')
