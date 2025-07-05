import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'ef667be475d8c3875aad1435b18b1e5'
HEADER = {'Content-Type':'application/json', 'trainer token':TOKEN}

body_registration = {
    "trainer_token":TOKEN,
    "email":"kristibah87@yandex.ru",
    "password":"kol56Bosa"
}


body_create = {
    "name": "Бульбазавр",
    "photo" : "https://dolnikov.ru/pokemons/albums/001.png"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)	
print(response_create.text)
