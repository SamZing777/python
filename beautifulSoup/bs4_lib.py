import requests
from bs4 import BeautifulSoup


request = requests.get("https://www.bbc.com/news")
soup = BeautifulSoup(request.content, 'html.parser')

divs = soup.select("divs", class_ = "item")
title = soup.select("h2", class_ = "section-title")
print(divs)
print(len(divs))
print(title)
print(len(title))

items = [item.text.strip() for item in soup.select('.item' )]
print(items)
print(len(items))


"""
other_soup = BeautifulSoup(soup, 'lxml')
job = other_soup.find("a", class_="story-list-story__info__headline-link")
print(job)
"""









































