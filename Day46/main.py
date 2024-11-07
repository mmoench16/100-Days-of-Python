from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# Billboard
year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{year}/", headers=header)
billboard100 = response.text

soup = BeautifulSoup(billboard100, "html.parser")

song_titles = soup.select("li h3#title-of-a-story")

songs = [song.getText().strip() for song in song_titles]

# print(len(songs))

# Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path=".cache"
    )
)

user_id = sp.current_user()["id"]
# print(user_id)

playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)

for song in songs:
    result = sp.search(q=f"track: {song} year: {year[:4]}", limit=1, type="track")
    try:
        song_uri = result["tracks"]["items"][0]["uri"]
        sp.playlist_add_items(playlist_id=playlist["id"], items=[song_uri])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")