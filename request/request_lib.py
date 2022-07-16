import requests

url = 'https://api.github.com/users/samzing777'
request = requests.get(url)

print("Request: ", request)
print("Content: ", request.content)
print("URL: ", request.url)
print("Status code: ", request.status_code)


print("Headers: ", request.headers)
print("Encoding: ", request.encoding)
print("Elapsed: ", request.elapsed)
print("Cookies: ", request.cookies)
print("History: ", request.history)
print("Redirect: ", request.is_redirect)
print("JSON: ", request.json())
print("Text: ", request.text)
print("Reason: ", request.reason)
print("Request: ", request.request)
print("Links: ", request.links)

