import json
import threading

from api import get_player_battle_log


class PopulateCountryLog(threading.Thread):
    def __init__(self, country, lock):
        threading.Thread.__init__(self)
        self.country = country
        self.lock = lock

    def run(self):
        battle_log_country(self.country, lock)


def populate_top_players():
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


def populate_battle_log():
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
        response = get_player_battle_log(player_tag)
        for battle in response:
            if battle['type'] == 'PvP' or battle['type'] == '2v2':
                battle_log.append(battle)
        print(n)
        n += 1

    with open('seeds/battle_logs/battle_log' + str(count) + '.json', 'w') as battle_log_file:
        json.dump(battle_log[n + 1:], battle_log_file)


def battle_log_country(country, lock):
    with open('seeds/top_players/' + country + '.json', 'r') as top_players_file:
        top_players_country = json.load(top_players_file)[country]
        battle_log = []
        for player in top_players_country:
            for battle in get_player_battle_log(player, lock):
                try:
                    if battle['type'] == 'PvP' and 'trophyChange' in battle['team'][0].keys() and battle['team'][0]['trophyChange'] != 0:
                        battle_log.append({
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
                except Exception as e:
                    print(e, country, player)
                    continue
        with open('seeds/battle_logs/' + country + '.json', 'w') as battle_log_file:
            json.dump(battle_log, battle_log_file)
    print('Done: ', country)


if __name__ == '__main__':
    # populate_top_players()
    # populate_battle_log()
    completed = ['Ascension Island', 'Canary Islands', 'Caribbean Netherlands', 'Ceuta and Melilla', 'Christmas Island',
                 'Diego Garcia', 'Eritrea', 'French Southern Territories', 'Heard & McDonald Islands',
                 'Pitcairn Islands', 'Saint Helena', 'Sint Maarten', 'South Sudan', 'Svalbard and Jan Mayen', 'Tokelau',
                 'Tristan da Cunha',
                 'U.S. Outlying Islands', 'Tuvalu', 'Cocos (Keeling) Islands', 'Kosovo', 'Norfolk Island',
                 'North Korea', 'Saint Barthélemy', 'Curaçao', 'Western Sahara', 'Niue', 'Montserrat',
                 'Falkland Islands',
                 'Antarctica', 'Bouvet Island', 'Guinea-Bissau', 'Kiribati', 'Wallis and Futuna',
                 'British Indian Ocean Territory',
                 'Vatican City', 'Burundi', 'Tonga', 'Solomon Islands', 'Comoros', 'Central African Republic', 'Palau',
                 'Samoa', 'Marshall Islands', 'Chad', 'Vanuatu', 'Gambia', 'Equatorial Guinea', 'Liberia',
                 'Saint Pierre and Miquelon', 'Lesotho', 'São Tomé and Príncipe', 'Micronesia', 'Rwanda',
                 'Sierra Leone', 'Anguilla', 'Nauru', 'British Virgin Islands', 'Cook Islands', 'Saint Kitts and Nevis']
    try:
        lock = threading.Lock()
        threads = []
        with open('seeds/countries.json') as countries_file:
            for country in json.load(countries_file):
                if country['name'] not in completed:
                    threads.append(PopulateCountryLog(country['name'], lock).start())
            for t in threads:
                t.join()
        print('Generated Battle Log')
    except Exception as e:
        print(e)
