import requests
from bs4 import BeautifulSoup
from pprint import pprint
# Importing the year and getting the URL
#date = '2010-07-07'
date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD\n")
URL = f'https://www.billboard.com/charts/hot-100/{date}/'

# Getting the HTML data from the website
response = requests.get(url=URL)
webpage = response.text

# Creating the soup
KLASA = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"
ID = "title-of-a-story"

soup = BeautifulSoup(webpage,'html.parser')
songs = soup.find_all(name='h3', class_=KLASA, id=ID)

# The first song is different
KLASA_1 = "c-title"
ID_1 = "title-of-a-story"
first_song = soup.find_all(name='h3', class_=KLASA_1)[0].get_text().split('\n')[2]
song_list=[first_song]
for song in songs:
    song_list.append(song.get_text().split('\n')[1])

# -------------------- SPOTIFY API --------------------------------------------------------------------------------------------------
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "Insert your client id"
CLIENT_SECRET = "Insert your client secret"
REDIRECT_URI = "http://example.com"
SCOPE = "playlist-modify-private"
USERNAME = "Insert your username"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
year = date.split('-')[0]

song_uris=[]

for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type='track')
    try:
        song_uris.append(result['tracks']['items'][0]['uri'])
    except IndexError:
        print(f"{song} doesn't exist in spotify.Skipped")


playlist= sp.user_playlist_create(user=user_id,
                        name=f"DeLorean car music. Year:{year}",
                        public=False,
                        description="Automated python project.Time travel to a date in time and get a playlist with the hottest 100 songs from that year according to Billboard."
                        )

sp.playlist_add_items(playlist_id=playlist["id"], items = song_uris, position=None)

print(URL)