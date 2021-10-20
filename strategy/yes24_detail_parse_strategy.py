from strategy.parse_strategy import ParseStrategy
from book.book_info import BookInfo
from bs4 import BeautifulSoup

class Yes24DetailParseStrategy(ParseStrategy):
    def __init__(self):
        pass

    def parse(self, dom: BeautifulSoup):
        title_item = dom.select('#yDetailTopWrap > div.topColRgt > div.gd_infoTop')
        body_item = dom.select('#yDetailTopWrap > div.topColRgt > div.gd_infoBot> div.gd_infoTbArea')
        book_info = BookInfo()

        # 출간일
        book_info.release_date = title_item[0].select_one('span.gd_pubArea > span.gd_date').text
        # 판매지수
        dom_el = book_info.selling_score = title_item[0].select_one('span.gd_sellNum')
        if dom_el:
            book_info.selling_score = dom_el.contents[2].replace("판매지수", "").strip()
        # 풀절여부
        # 정가
        #book_info.price = body_item[0].select_one('div:nth-child(4) > table > tbody > tr:nth-child(1) > td > span > em')
        book_info.price = body_item[0].select_one('div.gd_infoTb > table > tbody > tr:first-of-type > td:first-of-type > span > em.yes_m').text

        return book_info