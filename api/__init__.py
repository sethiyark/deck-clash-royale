import requests

from config import API_URL, HEADERS


def get_location_top_players(location_id):
    return requests.get(API_URL + '/locations/' + str(location_id) + '/rankings/players', headers=HEADERS).json()


def get_player_battle_log(player_tag, lock=None):
    try:
        if lock:
            lock.acquire()
        return requests.get(API_URL + '/players/' + player_tag + '/battlelog', headers=HEADERS).json()
    except Exception as e:
        print(e, 'Unable to get battle log')
        return []
    finally:
        if lock:
            lock.release()
