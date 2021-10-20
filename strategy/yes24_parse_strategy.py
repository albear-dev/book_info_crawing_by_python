from strategy.parse_strategy import ParseStrategy
from book.book_info import BookInfo
from bs4 import BeautifulSoup
from type.rank_type import RankType
from type.site_type import SiteType
from page.page_info import PageInfo
from sites.site_info import SiteInfo
from crawling_page_manager import CrawlingPageManager
from strategy.yes24_detail_parse_strategy import Yes24DetailParseStrategy
from crlogging.cr_logger import CRLogger

class Yes24ParseStrategy(ParseStrategy):
    __IDX_RANK__ = 0
    __IDX_ISBN__ = 1
    __IDX_PROD_NO__ = 2
    __IDX_PROD_NM__ = 3
    __IDX_SALE_PRICE__ = 4
    __IDX_YES_POINT__ = 5
    __IDX_AUTHOR__ = 6
    __IDX_PUB__ = 7
    __IDX_DESC__ = 8
    __IDX_SHIPPING_DATE__ = 9
    __IDX_CATEGORY__ = 10

    __logger = CRLogger.get_logger(__name__)

    def __init__(self):
        self.site_type = SiteType.YES24
        self.rank_type = RankType.NONE

    def parse(self, dom: BeautifulSoup):
        dom_list = dom.select('table > tr')

        book_list = list()
        page_manager = CrawlingPageManager()

        for i, row in enumerate(dom_list):
            if i == 0:
                continue

            self.__logger.debug('Processing [%s/%s][%d/%d]', SiteType.YES24, self.rank_type, i, len(dom_list)-1)
            item = row.find_all("td")
            book_info = BookInfo()

            # 순위
            book_info.rank = i
            # 상품번호
            book_info.prod_no = item[self.__IDX_PROD_NO__].text
            # 도서명
            book_info.prod_nm = item[self.__IDX_PROD_NM__].text
            # 할인가
            book_info.sale_price = item[self.__IDX_SALE_PRICE__].text
            # 저자들
            book_info.author = item[self.__IDX_AUTHOR__].text
            # 출판사
            book_info.publisher = item[self.__IDX_PUB__].text
            # 출고예상일
            book_info.shipping_date = item[self.__IDX_SHIPPING_DATE__].text

            #세부내용
            url_detail = "http://www.yes24.com/Product/Goods/" + book_info.prod_no
            page = page_manager.crowling_page(SiteInfo(SiteType.YES24), PageInfo(self.rank_type, url_detail, None, None, Yes24DetailParseStrategy()))
            book_info_detail = page.book_info_collection
            book_info.release_date = book_info_detail.release_date
            book_info.selling_score = book_info_detail.selling_score
            book_info.price = book_info_detail.price

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

        return book_list