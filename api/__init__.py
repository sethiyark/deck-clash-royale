import json

import requests

from config import *


def get_country_top_players(country):
    response = requests.get(API_URL + '/locations/' + str(country['id']) + '/rankings/players?limit=50',
                            headers=HEADERS).json()
    return {
        country['name']: [player['tag'] for player in response['items']]
    }


def get_global_top_players_api():
    try:
        with open('countries.json', 'r') as countries_data:
            countries = json.load(countries_data)
            with open('top_players.json', 'w') as top_players_file:
                json.dump([get_country_top_players(country) for country in countries], top_players_file)
            return 'Success'
    except Exception as e:
        print(e)
        return 'Failure'


def get_global_top_players():
    try:
        with open('top_players.json', 'w') as top_players_data:
            return json.load(top_players_data)
    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    print(get_global_top_players())
