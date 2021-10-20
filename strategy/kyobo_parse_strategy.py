from strategy.parse_strategy import ParseStrategy
from book.book_info import BookInfo
from bs4 import BeautifulSoup
from type.rank_type import RankType
from page.page_info import PageInfo
from crawling_page_manager import CrawlingPageManager
from strategy.kyobo_detail_parse_strategy import KyoboDetailParseStrategy
from crlogging.cr_logger import CRLogger

class KyoboParseStrategy(ParseStrategy):

    __IDX_RANK__          = 0
    __IDX_ISBN__          = 1
    __IDX_PROD_NM__       = 2
    __IDX_AUTHOR__        = 3
    __IDX_PUB__           = 4
    __IDX_RELEASE_DATE__  = 5
    __IDX_CATEGORY__      = 6
    __IDX_PRICE__         = 7

    __logger = CRLogger.get_logger(__name__)

    def __init__(self):
        pass

    def parse(self, dom: BeautifulSoup):
        dom_list = dom.select('table > tr')

        book_list = list()
        for i, row in enumerate(dom_list):
            if i <= 2:
                continue

            self.__logger.debug('Processing Kyobo...[%d/%d]', i, len(dom_list) - 1)
            item = row.find_all("td")
            book_info = BookInfo()

            # 순위
            book_info.rank = i
            # ISBN
            book_info.isbn = item[self.__IDX_ISBN__].text
            # 상품코드
            book_info.prod_no = "-"
            # 도서명
            book_info.prod_nm = item[self.__IDX_PROD_NM__].text
            # 저자들
            book_info.author = item[self.__IDX_AUTHOR__].text
            # 출판사
            book_info.publisher = item[self.__IDX_PUB__].text
            # 출판일
            book_info.release_date = item[self.__IDX_RELEASE_DATE__].text
            # 분야
            book_info.category = item[self.__IDX_CATEGORY__].text
            # 정가
            book_info.price = item[self.__IDX_PRICE__].text

            #세부내용
            #book_info_detail = self.parse_detail(book_info.isbn)
            book_info.selling_score = "-"
            book_info.sale_price = "-"

            book_list.append(book_info)

            # for debug
            '''
            print(book_info.rank)
            print(book_info.isbn)
            print(book_info.prod_nm)
            print(book_info.author)
            print(book_info.publisher)
            print(book_info.release_date)
            print(book_info.category)
            print(book_info.price)
            print()
            '''

        return book_list


    def parse_detail(self, prod_no):
        url_detail = "http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=" + prod_no
        return CrawlingPageManager.crowling_page(PageInfo(RankType.NONE, url_detail, None, None, KyoboDetailParseStrategy()))