
from classes import *

if __name__ == '__main__':
    bs = BookShelf()
    book = Book("Around the World in 80 Days")
    bs.appendBook(book)
    bs.appendBook(Book("Bible"))
    bs.appendBook(Book("Cinderella"))
    bs.appendBook(Book("Daddy-Long-Legs"))
    it = bs.iterator()

    while it.hasNext():
        book = it.next()
        print(book)
