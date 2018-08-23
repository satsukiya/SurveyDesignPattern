
from classes import *

if __name__ == '__main__':
    alice = NoSupport("Alice")
    bob = LimitSupport("Bob", 50)
    charlie = SpecialSupport("Charlie", 429)
    diana = LimitSupport("Diana", 200)
    elmo = OddSupport("Elmo")
    fred = LimitSupport("Fred", 300)

    alice.setNext(bob).setNext(charlie).setNext(diana).setNext(elmo).setNext(fred)

    for i in range(500):
        alice.support(Trouble(i))