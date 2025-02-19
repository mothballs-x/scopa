from deck import Card, ItalianDeck


class Player:

    def __init__(self, name, id):
        self.name = name
        self.player_id = id
        self.hand = []
        self.pile = []
        self.scopa: int
        self.points = 0

    def __repr__(self):
        return self.name

    def check_hand(self):
        print()
        print(f'{self.name}')
        print(f'{len(self.name) * "#"}')
        for i, card in enumerate(self.hand):
            print(i + 1, ': ', card)



