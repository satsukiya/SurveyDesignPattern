
from factory.classes import *
from listfactory.classes import *
from tablefactory.classes import *
import sys

if __name__ == '__main__':
    args = sys.argv

    if len(args) != 2:
        print("Usage: python main.py class.name.of.ConcreteFactory")
        print("Example 1: python main.py listfactory.classes.ListFactory")
        print("Example 2: python main.py tablefactory.classes.TableFactory")
    else :
        factory = Factory.getFactory(args[1]);

    asahi = factory.createLink("朝日新聞", "http://www.asahi.com/");
    yomiuri = factory.createLink("読売新聞", "http://www.yomiuri.co.jp/");

    us_yahoo = factory.createLink("Yahoo!", "http://www.yahoo.com/");
    jp_yahoo = factory.createLink("Yahoo!Japan", "http://www.yahoo.co.jp/");
    excite = factory.createLink("Excite", "http://www.excite.com/");
    google = factory.createLink("Google", "http://www.google.com/");

    traynews = factory.createTray("新聞");
    traynews.add(asahi);
    traynews.add(yomiuri);

    trayyahoo = factory.createTray("Yahoo!");
    trayyahoo.add(us_yahoo);
    trayyahoo.add(jp_yahoo);

    traysearch = factory.createTray("サーチエンジン");
    traysearch.add(trayyahoo);
    traysearch.add(excite);
    traysearch.add(google);

    page = factory.createPage("LinkPage", "結城 浩");
    page.add(traynews);
    page.add(traysearch);
    page.output();

