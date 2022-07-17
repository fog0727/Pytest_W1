import requests

r = requests.get("http://www.4399.com")

print(r.status_code)
print("--------------")
print(r.headers)
print("--------------")
print(r.url)
print("--------------")
print(r.cookies)
print("--------------")
print(r.text)