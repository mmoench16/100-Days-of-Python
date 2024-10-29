from bs4 import BeautifulSoup
import requests

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{year}/", headers=header)
billboard100 = response.text

soup = BeautifulSoup(billboard100, "html.parser")

song_titles = soup.select("li h3#title-of-a-story")

songs = [song.getText().strip() for song in song_titles]

print(len(songs))