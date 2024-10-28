from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
best_movies_page = response.text

soup = BeautifulSoup(best_movies_page, "html.parser")

movies = soup.select(selector="h3")

movie_list = [movie.get_text() for movie in movies]

# for movie in movies:
#     movie_list.append(movie.getText())

movie_list.reverse()

# print(movie_list)

with open("movies.txt", "w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")

# response = requests.get("https://news.ycombinator.com/")

# yc_web_page = response.text

# soup = BeautifulSoup(yc_web_page, "html.parser")

# elements_to_remove = soup.find_all("span", class_="sitebit comhead")

# for element in elements_to_remove:
#     element.extract()

# all_elements = soup.find_all(class_="athing")

# # print(all_elements[0])

# article_texts = []
# article_links = []

# for element in all_elements:
#     article_texts.append(element.find(class_="titleline").find("a").getText())
#     article_links.append(element.find(class_="titleline").find("a").get("href"))

# all_subtexts = soup.find_all(class_="subtext")

# article_upvotes = []

# for subtext in all_subtexts:
#     if subtext.find(class_="score") != None:
#         article_upvotes.append(int(subtext.find(class_="score").getText().split()[0]))
#     else:
#         article_upvotes.append(0)

# article_upvotes = [int(score.getText().split()[0]) for score in soup.select(selector="span.score")]

# print(len(article_texts))
# print(len(article_links))  
# print(len(article_upvotes))  

# print("-----")

# print(article_texts)
# print(article_links)  
# print(article_upvotes)

# print("-----")

# index_of_max_votes = article_upvotes.index(max(article_upvotes))
# print(index_of_max_votes)
# print(article_texts[index_of_max_votes])
# print(article_links[index_of_max_votes])

# ----------------------------------------------
# import lxml

# with open("website.html", "r") as file:
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# headings = soup.select(selector=".heading")
# print(headings)