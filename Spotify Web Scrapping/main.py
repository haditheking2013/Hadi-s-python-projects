import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

spotify_user = 'b5ac226e6e804f63823be1cc64f1b09c'
spotify_pass = 'e9705e3640624d7d8883abb0510691e2'

url = 'https://www.billboard.com/charts/hot-100/2000-08-12/'

response = requests.get(url)


contents = response.text
soup = BeautifulSoup(contents,'html.parser')

names_song = soup.find_all(name='h3', class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only')
songs = [ song.get_text().strip() for song in names_song]
for i in songs:
    print(i)

print(len(songs))

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=spotify_pass))
