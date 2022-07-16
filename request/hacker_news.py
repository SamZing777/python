import requests

request = requests.get("https://hacker-news.firebaseio.com/v0/item/")
print(request.content)
