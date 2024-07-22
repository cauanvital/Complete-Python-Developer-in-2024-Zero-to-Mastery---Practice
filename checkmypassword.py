import requests
import hashlib
import sys

def request_api_data(hash_query):
    res = requests.get(f'https://api.pwnedpasswords.com/range/{hash_query}')
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.content}')
    return res

def get_password_leak_count(response, hash_to_check):
    response = response.text.splitlines()
    splited_hashes = (line.split(':') for line in response)
    for h,count in splited_hashes:
        if hash_to_check['head'] + h == hash_to_check['full']:
            return count
    return 0

def password_converter(password):
    password_encoded = password.encode('utf-8')
    hash_pw = hashlib.sha1(password_encoded).hexdigest().upper()
    return {'head': hash_pw[:5], 'full': hash_pw}
    

def main(*args):
    for password in args:
        hash_pw = password_converter(password)
        response = request_api_data(hash_pw['head'])
        hash_leaks = get_password_leak_count(response, hash_pw)
        
        if hash_leaks == 0:
            print(f'No leaks of password {password}')
        else:
            print(f'{hash_leaks} leaks of password {password}')
    return 'Done!'

if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
