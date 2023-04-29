from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get("https://news.ycombinator.com/")
# response.raise_for_status()
# print(response.text)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
# article_tag = soup.find(name="span", class_="titleline").getText()
# print(article_tag)
# print(article_tag.getText())

article_text = []
article_link = []

for article_tag in articles:
    text = article_tag.getText()
    article_text.append(text)
    link = article_tag.find("a").get("href")
    article_link.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(int(article_upvotes[0].split()[0]))

# print(f"Article text is: {article_text}")
# print(f"Article link is: {article_link}")
# print(f"Upvotes for this article are: {article_upvotes}")

# Get article with most upvotes
max_upvotes = max(article_upvotes)
max_upvotes_index = article_upvotes.index(max_upvotes)
print(max_upvotes_index)

print(f"Article name: {article_text[max_upvotes_index]}\n"
      f"Link to article:{article_link[max_upvotes_index]}\n"
      f"with {max_upvotes} upvotes.")

# print(len(article_text),
#       len(article_link),
#       len(article_upvotes))

# write to csv
d = {"article_headings": article_text,
     "article_link": article_text}

# pd.DataFrame(d).to_csv("hacker_news_top_articles.csv")
