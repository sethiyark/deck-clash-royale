import requests

from config import API_URL, HEADERS
from libs.populate_data import populate_battle_log
from libs.populate_data import populate_top_players


# Work in progress
def get_unique_battles():
    response = requests.get(API_URL + '/players/%2389U0QL92/battlelog', headers=HEADERS).json()
    unique_battles = []
    for battle in response:
        if battle['type'] == 'PvP' and battle['team'][0]['trophyChange']:
            unique_battles.append({
                'winning_deck': [{
                    'name': card['name'],
                    'level': card['level'],
                    'maxLevel': card['maxLevel']
                } for card in battle['team'][0]['cards']] if battle['team'][0]['trophyChange'] > 0 else [{
                    'name': card['name'],
                    'level': card['level'],
                    'maxLevel': card['maxLevel']
                } for card in battle['opponent'][0]['cards']],
                'loosing_deck': [{
                    'name': card['name'],
                    'level': card['level'],
                    'maxLevel': card['maxLevel']
                } for card in battle['team'][0]['cards']] if battle['team'][0]['trophyChange'] < 0 else [{
                    'name': card['name'],
                    'level': card['level'],
                    'maxLevel': card['maxLevel']
                } for card in battle['opponent'][0]['cards']]
            })
    print(unique_battles)
    battle = {
        'loosing_deck': [{'name': 'The Log', 'level': 3, 'maxLevel': 5},
                         {'name': 'Hog Rider', 'level': 11, 'maxLevel': 11},
                         {'name': 'Archers', 'level': 13, 'maxLevel': 13},
                         {'name': 'Fireball', 'level': 11, 'maxLevel': 11},
                         {'name': 'Ice Spirit', 'level': 13, 'maxLevel': 13},
                         {'name': 'Musketeer', 'level': 11, 'maxLevel': 11},
                         {'name': 'Zap', 'level': 13, 'maxLevel': 13},
                         {'name': 'Barbarians', 'level': 13, 'maxLevel': 13}],
        'winning_deck': [{'name': 'Mortar', 'level': 13, 'maxLevel': 13},
                         {'name': 'Valkyrie', 'level': 11, 'maxLevel': 11},
                         {'name': 'Archers', 'level': 13, 'maxLevel': 13},
                         {'name': 'Goblin Gang', 'level': 13, 'maxLevel': 13},
                         {'name': 'Tornado', 'level': 8, 'maxLevel': 8},
                         {'name': 'Baby Dragon', 'level': 8, 'maxLevel': 8},
                         {'name': 'Poison', 'level': 8, 'maxLevel': 8},
                         {'name': 'Graveyard', 'level': 5, 'maxLevel': 5}]}

    print(len(unique_battles))


if __name__ == '__main__':
    get_unique_battles()