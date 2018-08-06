# deck-clash-royale
Deck building support for clash royale

[Click Here](https://developer.clashroyale.com/#/documentation) to refer documentation for Clash Royale api used.


### Features for training:
> 01. **DEFENSE** - # of cards with high health
> 02. **BRAWLER** - # of cards that target one troop/building at a time ie. PEKKA or PRINCE
> 03. **HARD_HITTER** - # of cards with high attack damage
> 04. **BUILDING_BUSTER** - # of cards that attack buildings
> 05. **BUILDING** - # of building  cards
> 06. **SWARM** - # of cards that spawn multiple units
> 07. **STUN** - # of cards that have stun or freeze ability
> 08. **SPLASH** - # of cards that have splash damage
> 09. **FLYING** - # of aerial cards
> 10. **GROUND** - # of ground cards
> 11. **AIR_DAMAGE** - # of cards that have air damage
> 12. **DAMAGE_SPELL** - # of damage spells
> 13. **STUN_SPELL** - # of stun spells
> 14. **CHEAP** - # of cards with low elixir cost (1-3)
> 15. **MODERATE** - # of cards with moderate elixir cost (4-5)
> 16. **HIGH** - # of cards with high elixir cost (5+)
> 17. **TRICKY** - # of cards has some unique attribute to it ie. Princess long range, Miner spawn freedom, etc
> 18. **HIGH_DPS** - # of cards with high DPS eg.Lumber Jack

### Hence our sample vector will have the following structure:
Each sample vector will be of size (1x36)
> **X** = [DEFENSE_A, BRAWLERS_A ... TRICKY_A, DEFENSE_B, BRAWLERS_B ... TRICKY_B]

> **Y** = 1 (Player A won)

> **Y** = 0 (Player B won)

[Battle Log](https://drive.google.com/open?id=1-Ilc_i0TPVhZAl9BmVk_VRXlkF34stL-)
Battle Log Collection for Training.
```
mongorestore --db deckCR --collection battle_log <path to dump>
```