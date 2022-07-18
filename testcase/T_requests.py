import requests
url = "http://www.4399.com"
r = requests.get(url)

print(r.status_code)
print("--------------")
print(r.headers)
print("--------------")
print(r.url)
print("--------------")
print(r.cookies)
print("--------------")
print(r.text)