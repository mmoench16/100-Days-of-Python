from bs4 import BeautifulSoup
# import lxml

with open("website.html", "r") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)

headings = soup.select(selector=".heading")
print(headings)