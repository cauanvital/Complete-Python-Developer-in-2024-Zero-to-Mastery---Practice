import re

pattern = re.compile(r'[A-Za-z0-9$%#@]{7,}\d')
password = input()
password_match = re.fullmatch(pattern, password)

if password_match != None:
    print('Valid password')
else:
    print('Invalid password')
