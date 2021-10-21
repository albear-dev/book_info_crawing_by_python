from strategy.parse_strategy import ParseStrategy
from book.book_info import BookInfo
from bs4 import BeautifulSoup
from type.rank_type import RankType
from page.page_info import PageInfo
from type.site_type import SiteType
from crawling_page_manager import CrawlingPageManager
from strategy.yes24_detail_parse_strategy import Yes24DetailParseStrategy
import csv
from crlogging.cr_logger import CRLogger

class AladinParseStrategy(ParseStrategy):

    # 엑셀 다운로드 후 컬럼 순서 정의
    __IDX_RANK__            = 0   # 순번/순위
    __IDX_DOMESTIC_TYPE__   = 1   # 구분
    __IDX_PROD_NM__         = 2   # 상품명
    __IDX_ISBN__            = 3   # ISBN
    __IDX_ISBN_13__         = 4   # ISBN13
    __IDX_ADDITIONAL_NO__   = 5   # 부가기호
    __IDX_PUB__             = 6   # 출판사 / 제작사
    __IDX_AUTHOR__          = 7   # 저자 / 아티스트
    __IDX_PRICE__           = 8   # 정가
    __IDX_SALE_PRICE__      = 9   # 판매가
    __IDX_SALE_AMT__        = 10  # 할인액
    __IDX_SALE_RT__         = 11  # 할인율
    __IDX_MILIIGE__         = 12  # 마일리지
    __IDX_RELEASE_DATE__    = 13  # 출간일
    __IDX_SALES_POINT__     = 14  # 세일즈포인트

    __logger = CRLogger.get_logger(__name__)

    def __init__(self):
        self.site_type = SiteType.ALADIN
        self.rank_type = RankType.NONE

    def parse(self, dom, ui_option):
        splitted_text = dom.text.split('\n')
        wrapper = csv.reader(splitted_text)
        book_list = list()

        for i, item in enumerate(wrapper):
            if i == 0:
                continue

            self.__logger.debug('Processing [%s/%s][%d/%d]', SiteType.ALADIN, self.rank_type, i, 1000)
            book_info = BookInfo()

            # 순위
            book_info.rank = item[self.__IDX_RANK__]
            # 상품번호
            book_info.prod_no = "-"
            # 도서명
            book_info.prod_nm = item[self.__IDX_PROD_NM__]
            # 정가
            book_info.price = item[self.__IDX_PRICE__]
            # 할인가
            book_info.sale_price = item[self.__IDX_SALE_PRICE__]
            # 저자들
            book_info.author = item[self.__IDX_AUTHOR__]
            # 출판사
            book_info.publisher = item[self.__IDX_PUB__]
            # 출간일
            book_info.release_date = item[self.__IDX_RELEASE_DATE__]
            # 세일즈포인트
            book_info.selling_score = item[self.__IDX_SALES_POINT__]

            book_list.append(book_info)

            # for debug
            '''
            print(book_info.rank)
            print(book_info.prod_no)
            print(book_info.prod_nm)
            print(book_info.price)
            print(book_info.sale_price)
            print(book_info.author)
            print(book_info.publisher)
            print(book_info.shipping_date)
            print(book_info.release_date)
            print(book_info.selling_score)
            print()
            '''

            if int(book_info.rank) >= 1000:
                break

        return book_list


    def parse_detail(self, prod_no):
        url_detail = "http://www.yes24.com/Product/Goods/" + prod_no
        return CrawlingPageManager.crowling_page(PageInfo(RankType.NONE, url_detail, None, None, Yes24DetailParseStrategy()))