import math


def get_updated_stat(stat, upgrade_lvl):
    upgraded_stat = stat
    for _ in range(upgrade_lvl - 1):
        upgraded_stat *= 1.1
        upgraded_stat = math.ceil(upgraded_stat - 0.5)
    return upgraded_stat

# TODO: Add function/s to extract all upgradable features of cards
