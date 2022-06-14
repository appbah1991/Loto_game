class CPUPlayer:

    def __init__(self, name, card):
        self.name = name
        self.card = card
        self.is_winner = None

    def turn(self, number):
        if number in self.card:
            self.card.cross_out(number)
            if self.card.is_empty():
                self.is_winner = True


class HumanPlayer(CPUPlayer):

    def turn(self,number):
        answer = input('Зачеркнуть? y/n')
        if answer == 'y':
            if number in self.card:
                self.card.cross_out(number)
                if self.card.is_empty():
                    self.is_winner = True
            else:
                self.is_winner = False
        else:
            if number in self.card:
                self.is_winner = False


def create_player(name, player_type, card):
    players = {
        '1':CPUPlayer,
        '0': HumanPlayer
    }
    player = players[player_type](name, card)
    return player