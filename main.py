import random
import requests


def create_pokemon():

    name_url = 'https://pokemonbattle.me:9104/pokemons'
    header = {'content-type': 'application/json', 'trainer_token': "ТОКЕН"}

    pokemon_names = ['Бульбазавр', 'Ивизавр', 'Венузавр', 'Чармандер', 'Чармелеон', 'Чаризард', 'Сквиртл',
                         'Вартортл',
                         'Бластойз',
                         'Катерпи', 'Метапод', 'Баттерфри', 'Видл', 'Какуна', 'Бидрилл', 'Пиджи', 'Пиджеотто', 'Пиджит',
                         'Раттата',
                         'Рэтикейт', 'Спироу', 'Фироу', 'Эканс', 'Эрбок', 'Пикачу', 'Райчу', 'Сэндшру', 'Сэндслэш',
                         'Нидоран' 'Нидорина',
                         'Нидоквин', 'Нидоран♂', 'Нидорино', 'Нидокинг', 'Клефейри', 'Клефейбл', 'Вульпикс',
                         'Найнтейлс',
                         'Джигглипуф',
                         'Вигглитаф', 'Зубат', 'Голбат', 'Оддиш', 'Глум', 'Вайлплум', 'Парас', 'Парасект', 'Венонат',
                         'Веномот', 'Диглетт',
                         'Дагтрио', 'Мяут', 'Персиан', 'Псидак', 'Голдак', 'Манки', 'Праймейп', 'Гроулит', 'Арканайн',
                         'Поливаг',
                         'Поливирл', 'Полирэт', 'Абра', 'Кадабра', 'Алаказам', 'Мачоп', 'Мачоук', 'Мачамп',
                         'Беллспраут',
                         'Випинбелл',
                         'Виктрибелл', 'Тентакул', 'Тентакруэль', 'Джеодуд', 'Гравелер', 'Голем', 'Понита', 'Рапидаш',
                         'Слоупок', 'Слоубро',
                         'Магнемайт', 'Магнетон', 'Фарфетчд', 'Додуо', 'Додрио', 'Сил', 'Дьюгонг', 'Граймер', 'Мак',
                         'Шеллдер', 'Клойстер',
                         'Гастли', 'Хонтер', 'Генгар', 'Оникс', 'Дроузи', 'Гипно', 'Крабби', 'Кинглер', 'Волторб',
                         'Электрод', 'Экзеггут',
                         'Экзеггутор', 'Кубон', 'Маровак', 'Хитмонли', 'Хитмончан', 'Ликитунг', 'Коффинг', 'Визинг',
                         'Райхорн', 'Райдон',
                         'Ченси', 'Танджела', 'Кангаскан', 'Хорси', 'Сидра', 'Голдин', 'Сикинг', 'Старью', 'Старми',
                         'Майм',
                         'Скайтер',
                         'Джинкс', 'Электабазз', 'Магмар', 'Пинсир', 'Торос', 'Мэджикарп', 'Гаярдос', 'Лапрас', 'Дитто',
                         'Иви', 'Вапореон',
                         'Джолтеон', 'Флареон', 'Поригон', 'Оманайт', 'Омастар', 'Кабуто', 'Кабутопс', 'Аэродактиль',
                         'Снорлакс',
                         'Артикуно', 'Запдос', 'Молдрес', 'Бульбазавр', 'Ивизавр', 'Венузавр', 'Чармандер', 'Чармелеон',
                         'Чаризард',
                         'Сквиртл', 'Вартортл', 'Бластойз', 'Катерпи', 'Метапод', 'Баттерфри', 'Видл', 'Какуна',
                         'Бидрилл',
                         'Пиджи',
                         'Пиджеотто', 'Пиджит', 'Раттата', 'Рэтикейт', 'Спироу', 'Фироу', 'Эканс', 'Эрбок', 'Пикачу',
                         'Райчу', 'Сэндшру',
                         'Сэндслэш', 'Нидоран', 'Нидорина', 'Нидоквин', 'Нидоран', 'Нидорино', 'Нидокинг', 'Клефейри',
                         'Клефейбл',
                         'Вульпикс', 'Найнтейлс', 'Джигглипуф', 'Вигглитаф', 'Зубат', 'Голбат', 'Оддиш', 'Глум',
                         'Вайлплум',
                         'Парас',
                         'Парасект', 'Венонат', 'Веномот', 'Диглетт', 'Дагтрио', 'Мяут', 'Персиан', 'Псидак', 'Голдак',
                         'Манки', 'Праймейп',
                         'Гроулит', 'Арканайн', 'Поливаг', 'Полирэт', 'Абра', 'Кадабра', 'Алаказам', 'Мачоп', 'Мачоук',
                         'Мачамп',
                         'Беллспраут', 'Випинбелл', 'Виктрибелл', 'Тентакул', 'Тентакруэль', 'Джеодуд', 'Гравелер',
                         'Голем',
                         'Понита',
                         'Рапидаш', 'Слоупок', 'Слоубро', 'Магнемайт', 'Магнетон', 'Фарфетчд', 'Додуо', 'Додрио', 'Сил',
                         'Дьюгонг',
                         'Граймер', 'Мак', 'Шеллдер', 'Клойстер', 'Гастли', 'Хонтер', 'Генгар', 'Оникс', 'Дроузи',
                         'Гипно',
                         'Крабби',
                         'Кинглер', 'Волторб', 'Электрод', 'Экзеггут', 'Экзеггутор', 'Кубон', 'Маровак', 'Хитмонли',
                         'Хитмончан',
                         'Ликитунг', 'Коффинг', 'Визинг', 'Райхорн', 'Райдон', 'Ченси', 'Танджела', 'Кангаскан',
                         'Хорси',
                         'Сидра', 'Голдин',
                         'Сикинг', 'Старью', 'Старми', 'Майм', 'Скайтер', 'Джинкс', 'Электабазз', 'Магмар', 'Пинсир',
                         'Торос', 'Мэджикарп',
                         'Гаярдос', 'Лапрас', 'Дитто', 'Иви', 'Вапореон', 'Джолтеон', 'Флареон', 'Поригон', 'Оманайт',
                         'Омастар', 'Кабуто',
                         'Кабутопс', 'Аэродактиль', 'Снорлакс', 'Артикуно', 'Запдос', 'Молдрес', 'Дратини', 'Драгонэйр',
                         'Драгонайт',
                         'Мьюту', 'Мью']

    under1000 = random.choice(range(1, 1000))

    rand_name = random.choice(pokemon_names)
    name_body = {
        "name": rand_name,
        "photo": f"https://dolnikov.ru/pokemons/albums/{under1000:03}.png"
    }
    response = requests.post(name_url, headers=header, json=name_body)
    print(response.json())
    return response.json()["id"]


def change_pokemon_name(pokemon_id):

    name_url = 'https://pokemonbattle.me:9104/pokemons'
    header = {'content-type': 'application/json', 'trainer_token': "ТОКЕН"}

    response = requests.put(name_url, headers=header, json={"pokemon_id":f"{pokemon_id}", "name":"Другое Имя"})
    print(response.json())


def catch_pokemon(pokemon_id):

    url_catch = "https://pokemonbattle.me:9104/trainers/add_pokeball"
    header = {'content-type': 'application/json', 'trainer_token': "ТОКЕН"}

    response = requests.post(url_catch, headers=header, json={"pokemon_id":f"{str(pokemon_id)}"})

    print(response.json())

def kill_pokemon(id):

    url_kill = "https://pokemonbattle.me:9104/pokemons/kill"
    header = {'content-type': 'application/json', 'trainer_token': "ТОКЕН"}

    response = requests.post(url_kill, headers=header, json={"pokemon_id":f"{str(id)}"})

    print(response.json())


poke_id = create_pokemon()
change_pokemon_name(poke_id)
catch_pokemon(poke_id)
