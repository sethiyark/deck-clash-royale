import json
import requests
import libs
from config import API_URL, HEADERS


def main():
    # libs.populateTopPlayers()
    libs.populateBattleLog()

    '''response = requests.get(API_URL + '/cards', headers=HEADERS).json()
    cards = [{
        'name': card['name'],
        'id': card['id'],
        'maxLevel': card['maxLevel']
    } for card in response['items']]
    with open('seeds/cards.json', 'w') as cards_file:
        json.dump(cards, cards_file)'''
    return 0


if __name__ == '__main__':
    main()
