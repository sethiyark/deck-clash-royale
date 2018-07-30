import requests

from config import *


def main():
    response = requests.get(API_URL + '/locations', headers=HEADERS).json()

    countries = []

    for c in response['items']:
        if c['isCountry']:
            countries.append({
                'id': c['id'],
                'name': c['name']
            })

    print(len(countries))
    return 0


if __name__ == '__main__':
    main()
