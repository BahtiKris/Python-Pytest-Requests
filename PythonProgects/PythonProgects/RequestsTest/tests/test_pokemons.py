import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ef667be475d8c3875aad1435b18b1e5'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 36374

body_registration = {
    "trainer_token":TOKEN,
    "email":"kristibah87@yandex.ru",
    "password":"kol56Bosa"
}


body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "114697",
    "name": "Пикачу",
    "photo_id": 4
}

body_add_pokebal = {
    "pokemon_id": "114800"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)   
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)  
print(response_change.text)'''

'''response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokebal)  
print(response_add_pokeball.text)'''

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID })
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/me', params = {'trainer_token':TOKEN })
    assert response_get.json()["data"][0]["trainer_name"] == 'Волшебник Оз'

