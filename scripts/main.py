import json


def main():
    # libs.populateTopPlayers()
    # libs.populate_battle_log()
    with open('seeds/battle_logs/India.json') as battle_log_file:
        print(len(json.load(battle_log_file)))
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
