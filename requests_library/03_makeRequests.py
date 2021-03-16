# https://httpbin.org/

import requests
'''
print("POST Method")
r = requests.post('https://httpbin.org/post')
print(r.status_code)
print(r.json())

print("=="*30)
print("DELETE Method")
r = requests.delete('https://httpbin.org/delete')
print(r.status_code)
print(r.json())

print("=="*30)
print("HEAD Method")
r = requests.head('https://httpbin.org/get')
print(r.status_code)
print(r.headers)  # head -> headers

'''

# r = requests.get('https://httpbin.org/get',data={'test':'123'})
# print(r.json())
# print(r.json())

'''
Passing Parameters In URLs
You often want to send some sort of data in the URL’s query string. If you were constructing the URL by hand, this data would be given as key/value pairs in the URL after a question mark, e.g. httpbin.org/get?key=val. Requests allows you to provide these arguments as a dictionary of strings, using the params keyword argument. As an example, if you wanted to pass key1=value1 and key2=value2 to httpbin.org/get, you would use the following code:

>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get('https://httpbin.org/get', params=payload)
You can see that the URL has been correctly encoded by printing the URL:

>>> print(r.url)
https://httpbin.org/get?key2=value2&key1=value1
Note that any dictionary key whose value is None will not be added to the URL’s query string.

'''
payload = {'ID': '18MA161', 'DOB': '12-12-2012'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)