import requests
'''
bad_r = requests.get('https://httpbin.org/status/404')
print(bad_r.status_code)
print(bad_r.text)
'''

# r = requests.get('https://postman-echo.com/basic-auth')
# print(r.text)
# print(r.status_code)

# header = {'Authorization':'Basic cG9zdG1hbjpwYXNzd29yZA=='}
# r = requests.get('https://postman-echo.com/basic-auth', headers=header)
# print(r.text)
# print(r.status_code)

# GET Method
# header = {'Authorization':'Basic cG9zdG1hbjpwYXNzd29yZA=='}
# payload = {'ID':'18MA161','NAME':"Nishanth M"}
# r_2 = requests.get('https://postman-echo.com/get', data=payload)
# print(r_2.status_code)
# print(r_2.text)

# POST Method
# header = {'Authorization':'Basic cG9zdG1hbjpwYXNzd29yZA=='}
# payload = {'ID':'18MA161','NAME':"Nishanth M"}
# r_2 = requests.post('https://postman-echo.com/post',headers=header, data=payload)
# print(r_2.status_code)
# print(r_2.text)

# Raw POST
header = {'Authorization':'Basic cG9zdG1hbjpwYXNzd29yZA=='}
files = {'file':open('05_testing.txt',mode='rb')}
r_2 = requests.post('https://postman-echo.com/post',headers=header, files=files) # it's returning the [content-type":"multipart/form-data]
print(r_2.status_code)
print(r_2.text)
