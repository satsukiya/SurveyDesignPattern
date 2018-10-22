from factory.classes import *

class TableLink(Link):

    def __init__(self, caption, url):
        super().__init__(caption, url)

    def makeHTML(self):
        mark = "<td><a href=\""
        mark += self._url
        mark += "\">"
        mark += self._caption
        mark += "</a></td>\n"
        return mark

class TablePage(Page):

    def __init__(self, title, author):
        super().__init__(title, author)

    def makeHTML(self):
        mark = "<html><head><title>"
        mark += self._title
        mark += "</title></head>\n"
        mark += "<body>\n"
        mark += "<h1>" + self._title + "</h1>"
        mark += "<table width=\"80%\" border=\"3\">\n"

        citr = iter(self._content)
        try :
            while True:
                val = next(citr)
                mark += val.makeHTML()
        except StopIteration:
            pass

        mark += "</table>\n"
        mark += "<hr><address>"
        mark += self._author
        mark += "</address>"
        mark += "</body></html>\n"
        return mark

class TableTray(Tray):

    def __init__(self, caption:str):
        print(caption)
        super().__init__(caption)

    def makeHTML(self):
        mark = "<td>"
        mark += "<table width=\"100%\" border=\"1\"><tr>"
        mark += "<td bgcolor=\"#cccccc\" align=\"center\" colspan=\""
        mark += str(len(self._tray))
        mark += "\"><b>"
        mark += self._caption
        mark += "</b></td>"
        mark += "</tr>\n"
        mark += "<tr>\n"

        titr = iter(self._tray)

        try :
            while True:
                var = next(titr)
                mark += var.makeHTML()
        except StopIteration:
            pass

        mark += "</tr></table>"
        mark += "</td>"
        return mark

class TableFactory(Factory):

    def createLink(caption:str, url:str):
        return TableLink(caption, url)

    def createTray(caption:str):
        print("createTray")
        return TableTray(caption)

    def createPage(title:str, author:str):
        return TablePage(title, author)
