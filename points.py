from collections import defaultdict

# Check for points
# Pass player to function or object
class Scoring:

    premiera = {'7': 21, '6': 18, '1': 16, '5': 15, '4': 14,
                '3': 13, '2': 12, 'F': 10, 'C': 10, 'R': 10}

    def __init__(self, players):
        self.players = players

    def greatest(self):
        piles = []
        for player in self.players:
            piles.append(len(player.pile))
        m = max(piles)
        i = piles.index(m)
        self.players[i].points += 1

    def sevens_denari(self):
        sevens = []
        for player in self.players:
            denari = [c for c in player.pile if c.suit == 'Denari']
            if 7 in denari:
                player.points += 1

        # cases: 1 player obviously has most
        # two players tied at most
        # two players tied but rest have most

        if sevens.count(max(sevens)) == 1:
            i = sevens.index(max(sevens))
            self.players[i] += 1

        elif sevens.count(max(sevens)) > 1:
            pass

    def premiera_count(self):

        primes = []
        for player in self.players:
            score = 0
            suit_dict = defaultdict(list)
            for c in player.pile:
                suit_dict[c.suit].append(c)
            for suit in suit_dict.keys():
                sorted_suit = sorted(suit_dict[suit], key=lambda c: self.premiera[c.rank], reverse=True)
                score += self.premiera[sorted_suit[0].rank]
            primes.append(score)
        i = primes.index(max(primes))
        self.players[i].points += 1

    def scopa(self):
        for player in self.players:
            player.points += player.scopa





















