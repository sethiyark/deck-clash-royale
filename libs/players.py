import json
import os

from api import get_location_top_players


def get_country_top_players(country):
    response = get_location_top_players(country['id'])
    return {
        country['name']: [player['tag'].replace('#', '%') for player in response['items']]
    }


def get_global_top_players_api():
    try:
        with open('seeds/countries.json', 'r') as countries_data:
            countries = json.load(countries_data)
            for country in countries:
                with open('seeds/top_players/' + country['name'] + '.json', 'w') as top_players:
                    json.dump(get_country_top_players(country), top_players)
                print(country['name'] + ' Done')
            return 'Success'
    except Exception as e:
        print(e)
        return 'Failure'


def get_global_top_players():
    top_players = []
    try:
        for country in os.listdir('seeds/top_players'):
            if country.endswith('.json'):
                with open('seeds/top_players/' + country, 'r') as top_players_data:
                    top_players.append(json.load(top_players_data))
        return top_players
    except Exception as e:
        print(e)
        return top_players


if __name__ == '__main__':
    print(get_global_top_players())
