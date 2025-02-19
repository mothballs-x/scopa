from deck import *
from table import *
from players import *
import time
from points import Scoring

def main() -> None:

    print()
    print()
    welcome = ' welcome to '
    print(f'{welcome:*^27}')
    time.sleep(1)
    print(r"""
 ___  ___ ___  _ __   __ _
/ __|/ __/ _ \| '_ \ / _` |
\__ \ (_| (_) | |_) | (_| |
|___/\___\___/| .__/ \__,_|
              | |
              |_|          """)
    print('Perchè no\' ghe xe gnente come \'na bea scopata')
    time.sleep(2)
    player_num = input('Enter number of players: ')
    players = []

    for i in range(int(player_num)):
        name = input(f'Player {i + 1}, enter your name: ')
        p = Player(name, i)
        players.append(p)

    table = Table(players)
    table.deal_hands()
    table.set_table()

    playing = True
    while playing:
        while len(table.deck) > 0:
            table.players[table.turn].check_hand()
            table.pick_up()
            table.check_round()
            table.show_pot()
            print(f'Cards left in deck: {len(table.deck)}')

        points = Scoring(players)
        points.greatest()
        points.sevens_denari()
        points.premiera_count()
        points.scopa()

        for player in table.players:
            if player.points >= 11:
                winner = player.name
                playing = False

    print(f'{len(winner) * "!"} + {35 * "!"}')
    time.sleep(1)
    print(f'!!!!!!!!!!!! HA VINTO {winner} !!!!!!!!!!!!!')
    time.sleep(1)
    print(f'{len(winner) * "!"} + {35 * "!"}')
    time.sleep(2)




if __name__ == '__main__':
    main()









