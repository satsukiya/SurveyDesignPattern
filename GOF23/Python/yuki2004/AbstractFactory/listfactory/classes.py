from factory.classes import *

class ListLink(Link):
    def __init__(self, caption:str, url:str):
        super().__init__(caption, url)

    def makeHTML(self):
        mark = " <li><a href=\""
        mark += self._url
        mark += "\">"
        mark += self._caption
        mark += "</a></li>\n"
        return mark

class ListPage(Page):
    def __init__(self, title:str, author:str):
        super().__init__(title, author)

    def makeHTML(self):
        mark = "<html><head><title>"
        mark += self._title + "</title></head>\n"
        mark += "<body>\n"
        mark += "<h1>" + self._title + "</h1>\n"
        mark += "<ul>\n"

        citr = iter(self._content)
        try :
            while True:
                val = next(citr)
                mark += val.makeHTML()
        except StopIteration:
            pass
        

        mark += "</ul>\n"
        mark += "<hr><address>" 
        mark += self._author
        mark += "</address>"
        mark += "</body></html>\n"
        return mark

class ListTray(Tray):
    def __init__(self, caption:str):
        super().__init__(caption)

    def makeHTML(self):
        mark = "<li>\n"
        mark += self._caption + "\n"
        mark += "<ul>\n"

        titr = iter(self._tray)
        try:
            while True:
                val = next(titr)
                mark += val.makeHTML()
        except StopIteration:
            pass
                
        mark += "</ul>\n"
        mark += "</li>\n"
        return mark


class ListFactory(Factory):

    def createLink(caption:str, url:str):
        return ListLink(caption, url)

    def createTray(caption:str):
        return ListTray(caption)

    def createPage(title:str, author:str):
        return ListPage(title, author)
