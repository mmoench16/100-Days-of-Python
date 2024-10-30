from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# Billboard
# year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{year}/", headers=header)
# billboard100 = response.text

# soup = BeautifulSoup(billboard100, "html.parser")

# song_titles = soup.select("li h3#title-of-a-story")

# songs = [song.getText().strip() for song in song_titles]

# print(len(songs))

# Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        # scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        scope="user-library-read"
        # show_dialog=True,
        # cache_path="token.txt"
    )
)

taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'

results = sp.artist_albums(taylor_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])

# user_id = sp.current_user()["id"]

# playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)

# sp.playlist_add_items(playlist_id=playlist["id"], items=[song for song in songs])