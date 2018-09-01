import os

from utils import MongoUtils

DB = MongoUtils('deckCR')

HQ_TAG = ' GQQQY9'
VIBE_TAG = ' 2YGJ8U0Q'
INDIA_ID = '57000113'
US_ID = '57000249'

API_URL = 'https://api.clashroyale.com/v1'

API_TOKEN = ''

if os.path.isdir(os.path.join(os.getcwd(), 'private')):
    try:
        import private

        API_TOKEN = private.API_TOKEN

    except Exception as e:
        print(e)

HEADERS = {
    'authorization': API_TOKEN,
    'Accept': 'application/json'
}

features = [
    "speed",
    "hitPoints",
    "hitSpeed",
    "damage",
    "range",
    "groundDamage",
    "count",
    "knockBack",
    "splashArea",
    "deathDamage",
    "targetsBuilding",
    "deathSpawn",
    "spawn",
    "heal",
    "airDamage",
    "airTroop",
    "spawnCount",
    "spawnTime",
    "chargeSpeedMultiplier",
    "chargeDamage",
    "boostUp",
    "shield",
    "freezeTime",
    "attackOnce",
    "spawnFreedom",
    "crownDamage",
    "canKnockBack",
    "projectileRange",
    "damageUpto",
    "multiTarget",
    "stunDuration",
    "spawnDamage",
    "lifeTime",
    "deployTime"
]
cards = []
for c in DB.find('cards', {}):
    cards.append(c)
