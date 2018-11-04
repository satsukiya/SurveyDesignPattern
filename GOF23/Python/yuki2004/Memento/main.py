
from game.classes import *
import time
import threading

if __name__ == '__main__':
    gamer = Gamer(100)
    memento = gamer.createMemento()

    for i in range(100):
        print("==== " + str(i))
        print("現状:" + str(gamer))

        gamer.bet()
        print("所持金は" + str(gamer.getMoney()) + "円になりました。")

        if gamer.getMoney() > memento.getMoney():
            print("    （だいぶ増えたので、現在の状態を保存しておこう）")
            memento = gamer.createMemento()

        elif gamer.getMoney() < memento.getMoney() / 2:
            print("    （だいぶ減ったので、以前の状態に復帰しよう）")
            gamer.restoreMemento(memento)

        time.sleep(1)
        print("")