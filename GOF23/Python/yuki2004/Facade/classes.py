import configparser

class Database:

    @staticmethod
    def getProperties(dbname:str):
        filename = dbname + ".txt"
        prop = None
        try :
            prop = configparser.ConfigParser()
            prop.read(filename)
        except configparser.Error as e:
            print(e)
        return prop

class HtmlWriter:
    
    def __init__(self, fio):
        self.__fio = fio

    def title(self, title:str):
        self.__fio.write("<html>")
        self.__fio.write("<head>")
        self.__fio.write("<title>" + title + "</title>")
        self.__fio.write("</head>")
        self.__fio.write("<body>\n")
        self.__fio.write("<h1>" + title + "</h1>\n")

    def paragraph(self, msg:str):
        self.__fio.write("<p>" + msg +"</p>\n")

    def link(self, href:str, caption:str):
        mark = "<a href=\""
        mark += href 
        mark += "\">"
        mark += caption
        mark += "</a>"
        self.paragraph(mark)

    def mailto(self, mailaddr:str, username:str):
        self.link("mailto:" + mailaddr, username)

    def close(self):
        self.__fio.write("</body>")
        self.__fio.write("</html>\n")
        self.__fio.close()

class PageMaker:
    
    @staticmethod
    def makeWelcomePage(mailaddr:str, filename:str):
        mailprop = Database.getProperties("maildata")
        username = mailprop['DEFAULT'][mailaddr]

        try :
            fout = open(filename, "w")

            writer = HtmlWriter(fout)
            writer.title("Welcome to " + username + "'s page!");
            writer.paragraph(username + "のページへようこそ。");
            writer.paragraph("メールまっていますね。");
            writer.mailto(mailaddr, username);
            writer.close();
        except IOError as e:
            print(e)
