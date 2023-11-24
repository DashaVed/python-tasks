import requests

text = input('Введите IP адрес: ')
response = requests.get(f'http://ip-api.com/json/{text}')

if response.json()['status'] == 'fail':
    print('Такого IP адреса не существует')
else:
    print(response.json()['country'])
