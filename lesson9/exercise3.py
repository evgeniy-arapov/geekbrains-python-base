import random

player = {
    'name': 'Player',
    'health': 100,
    'min_damage': 60,
    'max_damage': 70,
    'armor': 1.1
}

enemy = {
    'name': 'Enemy',
    'health': 204,
    'min_damage': 20,
    'max_damage': 30,
    'armor': 1.6
}


# player['name'] = input('What is your name?\n')


def attack(attacker, attacked):
    attacked['health'] -= (random.randint(attacker['min_damage'], attacker['max_damage'])) / attacked['armor']


winner = None
while player['health'] > 0:
    attack(player, enemy)

    if enemy['health'] > 0:
        attack(enemy, player)
    else:
        winner = player['name']
        break
else:
    winner = enemy['name']

print(f'Winner {winner}')
print(player)
print(enemy)
