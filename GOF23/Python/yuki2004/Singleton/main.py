
from classes import *

if __name__ == '__main__':
    obj1 = Singleton()
    obj2 = Singleton()

    m1 = MyClass()
    m2 = MyClass()

    if obj1 is obj2:
        print("同じインスタンスです。")
    else :
        print("同じインスタンスではありません。")

    print(id(obj1), id(obj2))

    if m1 is m2:
        print("同じインスタンスです。")
    else :
        print("同じインスタンスではありません。")

    print(id(m1), id(m2))