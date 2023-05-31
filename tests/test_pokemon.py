import pytest
import requests

def test_get_trainer_code():
    response = requests.get(url="https://pokemonbattle.me:9104/trainers",
                            headers={'content-type': 'application/json',
                                     'trainer_token':"849b128a59aea9d37655d8d39d180262"})

    assert response.status_code == 200, f"Код ответа {response.status_code}, вместо 200"


def test_get_trainer_id():

    response = requests.get(url="https://pokemonbattle.me:9104/trainers",
                            headers={'content-type': 'application/json',
                                     'trainer_token':"849b128a59aea9d37655d8d39d180262"},
                            params={"trainer_id":"4311"})

    assert response.json()["id"] == "4311", f"trainer_id не совпадает, 4311 != {response.json()['id']}"



