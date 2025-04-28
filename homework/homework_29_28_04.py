# Костромин Андрей Львович

import json
from random import choice


def gen_person():
    key = ''
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'l', 'm', 'n']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(key) != 10:
        key += choice(nums)

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    return {'key': key, 'name': name, 'tel': tel}


def write_json(person_dict):
    person_key = person_dict['key']
    person_value = {
        'name': person_dict['name'],
        'tel': person_dict['tel']
    }

    try:
        data = json.load(open("persons.json"))
    except FileNotFoundError:
        data = {}

    data[person_key] = person_value
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())