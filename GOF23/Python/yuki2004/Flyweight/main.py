
from classes import *

import sys

if __name__ == '__main__':
    args = sys.argv

    if len(args) != 2:
        print("Usage: python main.py digits")
        print("Example: python main.py 1212123")
    else :
        bs = BigString(args[1])
        bs.fprint()
