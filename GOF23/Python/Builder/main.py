from classes import *
import sys

def usage():
    print("Usage: python main.py plain      プレーンテキストで文書作成")
    print("Usage: python main.py html       HTMLファイルで文書作成")


if __name__ == '__main__':
    args = sys.argv

    if len(args) != 2:
        usage()
    else :
        if args[1] == "plain":
            textbuilder = TextBuilder()
            director = Director(textbuilder)
            director.construct()
            print(textbuilder.getResult())
        elif args[1] == "html":
            htmlbuilder = HTMLBuilder()
            director = Director(htmlbuilder)
            director.construct()
            print(htmlbuilder.getResult() + "が作成されました。")
        else :
            usage()





"""
    textbuilder = TextBuilder()
    director = Director(textbuilder)
    director.construct()
    print(textbuilder.getResult())
"""