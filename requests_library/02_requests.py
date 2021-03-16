import requests
search_url_1 = 'https://en.wikipedia.org/wiki/Tamil_Nadu'


# r = requests.get(url=search_url_1)

# print(r.headers['content-type'])
# print(r.headers.get('content-type'))  # best pratice
# print(r.encoding)

# Return page source code in text format
# print(r.text)

# Return page source code in byte format
# print(r.content)

# print(r.content == r.text)
# print(f"Content type : {type(r.content)}") # real time use case: download image it's in byte format
# print(f"Text type : {type(r.text)}")

#print(r.json()) # Through an error json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0) because it's in HTML format

search_url_2 = 'https://api.github.com/user'
r_2 = requests.get(url=search_url_2, auth=('user', 'pass'))
print(r_2.json()) # Return json format