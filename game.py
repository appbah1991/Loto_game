from bag import Bag
from card import Card
from player import create_player


def is_continue_game(players):
    for item in players:
        if not (item.is_winner is None):
            return False
    return True


bag = Bag(90)
player_count = int(input('Введите количество игроков: '))
players = []
for i in range(player_count):
    name = input(f'Введите имя игрока {i + 1}: ')
    player_type = input(f'Введите тип игрока CPU - 1, Human - 0: ')
    card = Card(bag.get_random_numbers(15))
    player = create_player(name, player_type, card)
    players.append(player)

while is_continue_game(players):
    number = bag.get_next_number()
    print(f'Следующий Номер: {number}')
    for player in players:
        print(f'Карточка игрока {player.name}')
        print(player.card)
        player.turn(number)


has_winner = False
has_looser = False
for player in players:
    if player.is_winner is None:
        pass
    else:
        if player.is_winner:
            has_winner = True
        else:
            has_looser = True

if has_winner:
    for player in players:
        if player.is_winner:
            print(player.name, 'Win!')
        else:
            print(player.name, 'Loose!')
elif has_looser:
    for player in players:
        if player.is_winner is None:
            print(player.name, 'Win!')
        else:
            print(player.name, 'Loose!')
else:
    print('Что то пошло не так')



