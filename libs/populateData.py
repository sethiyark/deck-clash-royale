import json
import requests
from config import API_URL, HEADERS


def populateTopPlayers():
    with open('seeds/countries.json', 'r') as countries_file:
        countries = json.load(countries_file)
        top_player_tags = []
        for country in countries:
            with open('seeds/top_players/' + country['name'] + '.json', 'r') as top_players_file:
                top_players_for_country = json.load(top_players_file)
                for player in top_players_for_country[country['name']]:
                    top_player_tags.append(player)
        with open('seeds/top_players.json', 'w') as top_players_out:
            json.dump(top_player_tags, top_players_out)

        print("Total player tags: " + str(len(top_player_tags)))
    return 0


def populateBattleLog():
    n = 8001
    count = 10
    top_players = []
    battle_log = []

    with open('seeds/top_players.json', 'r') as top_players_file:
        top_players = json.load(top_players_file)

    top_players = top_players[8000:]

    for player_tag in top_players:
        if n % 500 == 0:
            with open('seeds/battle_logs/battle_log' + str(count) + '.json', 'w') as battle_log_file:
                json.dump(battle_log, battle_log_file)
            count += 1
        response = requests.get(API_URL + '/players/' + player_tag + '/battlelog', headers=HEADERS).json()
        for battle in response:
            if battle['type'] == 'PvP' or battle['type'] == '2v2':
                battle_log.append(battle)
        print(n)
        n += 1

    with open('seeds/battle_logs/battle_log' + str(count) + '.json', 'w') as battle_log_file:
        json.dump(battle_log[n + 1:], battle_log_file)


if __name__ == '__main__':
    populateTopPlayers()
    populateBattleLog()
