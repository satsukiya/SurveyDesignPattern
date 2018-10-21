
from classes import *

if __name__ == '__main__':
    ws = WinnerStrategy()
    pb = ProbStrategy()

    player1 = Player("Alice", ws)
    player2 = Player("Bob", pb)

    for i in range(10000):
        hand1 = player1.nextHand()
        hand2 = player2.nextHand()
        result = fight(hand1,hand2)
        if result == 1:
            print("winner:" + player1.name)
            player1.win()
            player2.lose()
        elif result == -1:
            print("winner:" + player2.name)
            player1.lose()
            player2.win()
        else :
            print("even")
            player1.even()
            player2.even()

    print(player1)
    print(player2)


