import requests


def super_hero_intelligence(heroes):
    response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    intelligence = 0
    name = ''
    for hero in response.json():
        if hero['name'] in heroes and hero['powerstats']['intelligence'] > intelligence:
            intelligence = hero['powerstats']['intelligence']
            name = hero['name']
    return f'Самый умный {name} с интелектом {intelligence}'


if __name__ == '__main__':
    print(super_hero_intelligence(['Hulk', 'Thanos', 'Captain America']))
