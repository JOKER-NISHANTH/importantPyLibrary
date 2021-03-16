import requests

# r = requests.get("https://httpbin.org/get")
'''
print(r.text) # new line

print(r.content)

print(r.json())
'''

header = {'Accept': 'application-type/json'}
payload = {'name':'Africa','mobile_no':'9876543210'}
'''
r = requests.get('https://httpbin.org/get', headers=header)
print(r.text)
print(r.url)
'''
'''
r = requests.post('https://httpbin.org/post',headers=header,data=payload)
print(r.text)
print(r.url)
'''
# upload img
files = {'file':open(r'praticalEgs/hack1.jpg',mode='rb')}
r = requests.post('https://httpbin.org/post', headers=header, data=payload, files=files)
print(r.status_code)
print(r.text)
print(r.url)
