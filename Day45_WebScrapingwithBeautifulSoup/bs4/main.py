from bs4 import BeautifulSoup
# import lxml

with open("website.html", encoding="utf8") as file:
    contents = file.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser")
# print(soup)
# print(soup.prettify())
# print(soup.title.name)
# print(soup.title.string)
# print(soup.p)
# print(soup.a)
# print(soup.h1)

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    ...

heading = soup.find_all(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))

# Using CSS selector
# para with anchor: This uses a CSS selector to find all the <a> tags in a <p> tag.
company_url = soup.select_one(selector="p a")
# print(company_url)

name = soup.select_one(selector="#name")
# print(name)

headings = soup.select(".heading")
# print(headings)








