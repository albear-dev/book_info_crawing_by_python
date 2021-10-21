from strategy.parse_strategy import ParseStrategy
from book.book_info import BookInfo
from bs4 import BeautifulSoup
from type.rank_type import RankType
from type.site_type import SiteType
from crlogging.cr_logger import CRLogger

class Yes24DetailParseStrategy(ParseStrategy):
    __logger = CRLogger.get_logger(__name__)

    def __init__(self):
        self.site_type = SiteType.YES24
        self.rank_type = RankType.NONE

    def parse(self, dom: BeautifulSoup, component_binder):
        title_item = dom.select('#yDetailTopWrap > div.topColRgt > div.gd_infoTop')
        body_item = dom.select('#yDetailTopWrap > div.topColRgt > div.gd_infoBot> div.gd_infoTbArea')
        book_info = BookInfo()

        try:
            # 출간일
            book_info.release_date = title_item[0].select_one('span.gd_pubArea > span.gd_date').text
        except BaseException as e:
            self.__logger.error("Error parse text [출간일][%s]", str(e))
            book_info.release_date = "-"

        try:
            # 판매지수
            dom_el = book_info.selling_score = title_item[0].select_one('span.gd_sellNum')
            if dom_el:
                book_info.selling_score = dom_el.contents[2].replace("판매지수", "").strip()
        except BaseException as e:
            self.__logger.error("Error parse text [판매지수][%s]", str(e))
            book_info.selling_score = "-"

        try:
            # 정가
            #book_info.price = body_item[0].select_one('div:nth-child(4) > table > tbody > tr:nth-child(1) > td > span > em')
            book_info.price = body_item[0].select_one('div.gd_infoTb > table > tbody > tr:first-of-type > td:first-of-type > span > em.yes_m').text
        except BaseException as e:
            self.__logger.error("Error parse text [정가][%s]", str(e))
            book_info.price = "-"

        return book_info