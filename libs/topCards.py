import numpy as np
from bson.code import Code

from config import DB
from config import features


def generate_cards_count():
    mapper = Code("""
                    function() {
                        this.winning_deck.forEach(function(c) {
                            emit(c.name, 1);
                        });
                        this.loosing_deck.forEach(function(c) {
                            emit(c.name, 1);
                        });
                    }""")
    reduce = Code("""
                    function(key, values) {
                        return Array.sum(values);
                    }
                    """)
    return DB.map_reduce('battle_log', mapper, reduce, 'card_count')


def get_cards_count():
    return DB.find('card_count', {})


def get_card_features(card, card_count):
    card_features = []
    have_features = []
    c_features = card.keys()
    m_features = set()
    if 'mixed' in c_features:
        for f in card['mixed']:
            for key in f.keys():
                m_features.add(key)
    for feature in features:
        if feature in m_features:
            have_features.append(1)
            card_features.append(0)
            for c in card['mixed']:
                if feature in c.keys():
                    if type(c[feature]) is bool:
                        card_features[-1] += (1 if c[feature] else 0)
                        if not c[feature]:
                            have_features[-1] += 0
                        continue
                    card_features[-1] += c[feature]
            continue
        if feature in c_features:
            have_features.append(1)
        else:
            have_features.append(0)
            card_features.append(0)
            continue
        if feature == 'spawn' or feature == 'deathSpawn':
            card_features.append(0)
            if type(card[feature]) is dict:
                try:
                    card_features[-1] = int(
                            card[feature]['damage'] / card[feature]['hitSpeed'] * card[feature]['hitPoints'])
                except:
                    card_features[-1] = 0
            if card_features[-1] == 0:
                have_features[-1] = 0
        else:
            if type(card[feature]) is bool:
                card_features.append(1 if card[feature] else 0)
                if not card[feature]:
                    have_features[-1] = 0
                continue
            card_features.append(card[feature])
    card_features.append(0)
    have_features.append(0)
    for c in card_count:
        if c['_id'] == card['name']:
            card_features[-1] = (c['value'])
            have_features[-1] = 1
    return card_features, have_features


def get_cards_matrix():
    cards = DB.find('cards', {})
    card_count = get_cards_count()
    features_matrix = []
    have_matrix = []
    for card in cards:
        card_features, have_features = get_card_features(card, card_count)
        features_matrix.append(card_features)
        have_matrix.append(have_features)
    feature_matrix_array = np.array(features_matrix, np.int)
    return feature_matrix_array


if __name__ == '__main__':
    print(get_cards_matrix())
