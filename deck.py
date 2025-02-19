# Classes for deck creation
from collections import UserList
import random
import functools
from typing import Union


class Card:

    rank_dict = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
                 6: '6', 7: '7', 8: 'F', 9: 'C', 10: 'R'}

    value_dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                  '6': 6, '7': 7, 'F': 8, 'C': 9, 'R': 10}

    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit
        self._value: int = self.value_dict[rank]

    @property
    def value(self):
        return self._value

    def __add__(self, other: Union["Card", int]):
        if isinstance(other, Card):
            return self._value + other._value
        elif isinstance(int, other):
            return self._value + other

    def __radd__(self, other: Union["Card", int]):
        if isinstance(other, Card):
            return other._value + self._value
        elif isinstance(other, int):
            return other + self._value

    def __gt__(self, other):
        return self._value > other._value

    def __lt__(self, other: "Card"):
        return self._value < other._value

    def __eq__(self, other: "Card"):
        if isinstance(other, Card):
            return self._value == other._value or other._value == self._value
        elif isinstance(other, int):
            return self.value == other or other == self._value

    def __repr__(self):
        return f'Card(rank={self.rank}, suit={self.suit})'

    def __str__(self):
        return f'{self.rank} di {self.suit}'


class ItalianDeck:

    ranks = [x for x in '1234567FCR']
    suits = ['Bastoni', 'Coppe', 'Spade', 'Denari']

    def __init__(self) -> None:
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __getitem__(self, index):
        return self.cards[index]

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self) -> Card:
        return self.cards.pop()




