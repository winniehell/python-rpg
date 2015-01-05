from pprint import pprint

from rpg.creatures import load

all_players = load('data/players.json')
all_monsters = load('data/monsters.json')


player = all_players[0]
monster = all_monsters[0]

while player.is_alive() and monster.is_alive():
    pprint(player)
    pprint(monster)
    player.actions[0].execute(monster)
    monster.actions[0].execute(player)
    print()

if not player.is_alive():
    print(player.name+' died!')

if not monster.is_alive():
    print(monster.name+' died!')