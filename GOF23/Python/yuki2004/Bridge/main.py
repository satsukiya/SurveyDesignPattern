from classes import * 

if __name__ == '__main__':
    d1 = Display(StringDisplayImpl("Hello, Japan."))
    d2 = CountDisplay(StringDisplayImpl("Hello, World."))
    d3 = CountDisplay(StringDisplayImpl("Hello, Universe."))
    d1.display()
    d2.display()
    d3.display()
    d3.multiDisplay(5)