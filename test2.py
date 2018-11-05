import requests

r = requests.get('https://api.github.com/events')
# r.raise_for_status()
# print(r.status_code)
print(r.raw)
print(r.raw.read())
print(r.content)
print(r.text)
print(r.json())
r.close()

payload = {
   'allowinsubframe': 'null',
   'localStorage': 'true',
   'login': 'jsp',
   'loginstamp': '1540869068997',
   'mobile': 'false',
   'password': '111111',
   'username': 'dingjianguang'}
r = requests.get("http://httpbin.org/get",params=payload)
# r = requests.get("http://httpbin.org/get",data=payload)
print(r.url)
print(r.text)
print(r.json())
r.close()

