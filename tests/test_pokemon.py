import pytest
import requests

TOKEN = "849b128a59aea9d37655d8d39d180262"
ID = "4311"

def test_get_trainer_code():
    response = requests.get(url="https://pokemonbattle.me:9104/trainers",
                            headers={'content-type': 'application/json',
                                     'trainer_token':TOKEN})

    assert response.status_code == 200, f"Код ответа {response.status_code}, вместо 200"


def test_get_trainer_id():

    response = requests.get(url="https://pokemonbattle.me:9104/trainers",
                            headers={'content-type': 'application/json',
                                     'trainer_token':"849b128a59aea9d37655d8d39d180262"},
                            params={"trainer_id":ID})

    assert response.json()["id"] == "4311", f"trainer_id не совпадает, {ID} != {response.json()['id']}"



