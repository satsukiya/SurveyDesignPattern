
from classes import *

if __name__ == '__main__':
    
    readline = None

    with open("program.txt", "r") as fin:
        readline = fin.read().split("\n")

    for text in readline:
        print("text = \"" + text + "\"")
        node = ProgramNode()
        node.parse(Context(text))
        print("node = " + str(node))