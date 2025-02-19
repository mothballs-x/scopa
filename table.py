import re
from typing import List
from deck import ItalianDeck, Card
from players import Player
from pprint import pprint

class Table:

    def __init__(self, players: Player):
        self.deck = ItalianDeck()
        self.players: List = players      # make list in main and then import
        self.pot: list = None
        self.turn = 0     # Player.player_id of person whose turn it is
        self.round = 0

    def set_table(self):
        self.deck.shuffle()
        self.pot = [self.deck.deal() for _ in range(4)]
        self.show_pot()

    def show_pot(self):
        print('TABLE')
        print('#####')
        for i, card in enumerate(self.pot, start=1):

            print(i, ': ', card)
        print()


    def pick_up(self):

        choice = input(f'{self.players[self.turn].name}, Choose card(s) by index or pass: ')
        RE = re.compile(r'(^\w{4}$|\d+)')
        choices = RE.findall(choice)
        check = True
        if choices[0] == 'pass':
            print('Please chose a card to drop: ')
            drop_card = int(input())
            drop_card = drop_card - 1
            try:
                self.pot.append(self.players[self.turn].hand[drop_card])
                del self.players[self.turn].hand[drop_card]
            except IndexError:
                print('Please choose card number, not rank...')
                return None
        else:
            choices = [int(n) - 1 for n in choices]

            if len(choices) == 1:
                check = self.match(choices[0])

            elif len(choices) > 1:
                check = self.add_match(choices)

        if not self.pot:
            for _ in range(4):
                print('SCOPA SCOPA SCOPA SCOPA SCOPA')
                print()
                print(f'SCOPA PER GIUOCATORE {self.turn}')
                self.players[self.turn].scopa += 1

        if check:
            self.turn += 1
            if self.turn > len(self.players) - 1:
                self.turn = 0

    def match(self, choice):
        match_card = self.pot[choice]
        player_id = self.turn
        hand_check = self.players[player_id].hand
        # check for doubles or triples
        if hand_check.count(match_card):
            i = hand_check.index(match_card)
            pile_card = self.players[player_id].hand[i]
            self.players[player_id].pile.append(match_card)
            self.players[player_id].pile.append(pile_card)
            self.pot.remove(match_card)
            self.players[player_id].hand.remove(pile_card)
        else:
            print('Not a valid match.')
            return False
        return True

    def add_match(self, choices):
        # sum the chosen cards
        player = self.turn

        pot_card_sum = sum([self.pot[i] for i in choices])
        current_hand = self.players[player].hand

        for card in current_hand:
            if card in self.pot:
                print('Sorry you must match a single card or pass.')
                return False


        matches = []
        for card in current_hand:
            if card == pot_card_sum:
                matches.append(card)

        if len(matches) == 0:
            print('Sorry, none of your cards equal the sum of the pot cards selected.')
            return False

        if len(matches) > 1:
            print("The following cards in your hand match the pot cards:")
            print([card for card in current_hand if card == pot_card_sum])
            card_num = int(input('Which card would you like to pair: '))
            card_num = card_num - 1
        else:
            card_num = 0

        self.players[player].pile.extend(choices)
        self.players[player].pile.append(matches[card_num])
        self.players[player].hand.remove(matches[card_num])
        remove = [self.pot[i] for i in choices]
        for card in remove:
            self.pot.remove(card)

        return True

    def check_round(self):
        if sum([len(p.hand) for p in self.players]) == 0:
            self.deal_hands()

    def deal_hands(self):
        """ Deals out first hand and subsequent hands when players are out of cards"""

        self.deck.shuffle()
        for player in self.players:
            firsthand = [self.deck.deal() for _ in range(3)]
            player.hand.extend(firsthand)









