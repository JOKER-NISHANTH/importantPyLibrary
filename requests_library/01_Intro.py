"""
Lets learn
"""

'''

['ConnectTimeout', 'ConnectionError', 'DependencyWarning', 'FileModeWarning', 'HTTPError', 'NullHandler', 'PreparedRequest', 'ReadTimeout', 'Request', 'RequestException', 'RequestsDependencyWarning', 'Response', 'Session', 'Timeout', 'TooManyRedirects', 'URLRequired', '__author__', '__author_email__', '__build__', '__builtins__', '__cached__', '__cake__', '__copyright__', '__description__', '__doc__', '__file__', '__license__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__title__', '__url__', '__version__', '_check_cryptography', '_internal_utils', 'adapters', 'api', 'auth', 'certs', 'chardet', 'check_compatibility', 'codes', 'compat', 'cookies', 'delete', 'exceptions', 'get', 'head', 'hooks', 'logging', 'models', 'options', 'packages', 'patch', 'post', 'put', 'request', 'session', 'sessions', 'ssl', 'status_codes', 'structures', 'urllib3', 'utils', 'warnings']

print(dir(requests))
'''
print("Welcome to learn Requests Library")

import requests

search_url = 'https://en.wikipedia.org/wiki/Tamil_Nadu'
r = requests.get(url=search_url)

#  now call the object(requests.get) and here r is instance to store the values
print("=="*30)
print(r)
print("=="*30)
print(type(r))
print("=="*30)
print(r.status_code)
print("==" *30)
print(type(r.status_code))
print("==" * 30)
print(help(r))
print("==" *30)
print(dir(r))
print("==" *30)
