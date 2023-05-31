import pytest
import requests

def test_get_trainer_code():
    response = requests.get(url="https://pokemonbattle.me:9104/trainers",
                            headers={'content-type': 'application/json',
                                     'trainer_token':"ТОКЕН"})

    assert response.status_code == 200, f"Код ответа {response.status_code}, вместо 200"


def test_get_trainer_id():

    response = requests.get(url="https://pokemonbattle.me:9104/trainers",
                            headers={'content-type': 'application/json',
                                     'trainer_token':"ТОКЕН"},
                            params={"trainer_id":"ВАШ_ID"})

    assert response.json()["id"] == "ВАШ_ID", f"trainer_id не совпадает, ВАШ_ID != {response.json()['id']}"



