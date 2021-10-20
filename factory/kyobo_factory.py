from sites.site_info import SiteInfo
from page.page_info import PageInfo
from type.site_type import SiteType
from type.rank_type import RankType
from type.book_store_type import BookStoreType
from strategy.kyobo_parse_strategy import KyoboParseStrategy
from util.date_util import DateUtil


class KyoboFactory:
    def __init__(self):
        pass

    __fetch_size = 200
    __fetch_key = "perPage"

    __url = "http://www.kyobobook.co.kr"
    #__url_monthly = __url + "/bestSellerNew/bestSellerExcel.laf?targetPage=1&mallGb=KOR&range=1&kind=2&selBestYmw="+DateUtil.get_prev_ym()+"&linkClass=A&pageNumber=1&perPage=1000&excelYn=Y"
    __url_monthly = __url + "/bestSellerNew/bestSellerExcel.laf?targetPage=1&mallGb=KOR&range=1&kind=2&linkClass=A&pageNumber=1&perPage=1000&excelYn=Y"
    #__url_weekly = __url + "/bestSellerNew/bestSellerExcel.laf?targetPage=1&mallGb=KOR&range=1&kind=0&selBestYmw="+DateUtil.get_ymw()+"&linkClass=A&pageNumber=1&perPage=1000&excelYn=Y"
    __url_weekly = __url + "/bestSellerNew/bestSellerExcel.laf?targetPage=1&mallGb=KOR&range=1&kind=0&linkClass=A&pageNumber=1&perPage=1000&excelYn=Y"
    __url_iweekly = __url + "/bestSellerNew/bestSellerExcel.laf?targetPage=1&mallGb=KOR&range=0&kind=0&linkClass=0&pageNumber=1&perPage=1000&excelYn=Y"
    __url_idaily = __url + "/bestSellerNew/bestSellerExcel.laf?targetPage=1&mallGb=KOR&range=0&kind=1&linkClass=0&pageNumber=1&perPage=1000&excelYn=Y"

    def create_site_info(self):
        _site_info = SiteInfo(SiteType.KYOBO)
        _site_info.add_page(PageInfo(RankType.MONTHLY, self.__url_monthly, self.__fetch_key, self.__fetch_size, KyoboParseStrategy()))
        _site_info.add_page(PageInfo(RankType.WEEKLY, self.__url_weekly, self.__fetch_key, self.__fetch_size, KyoboParseStrategy()))
        _site_info.add_page(PageInfo(RankType.IWEEKLY, self.__url_iweekly, self.__fetch_key, self.__fetch_size, KyoboParseStrategy()))
        _site_info.add_page(PageInfo(RankType.IDAILY, self.__url_idaily, self.__fetch_key, self.__fetch_size, KyoboParseStrategy()))
        return _site_info

    def calc_ymw(self):
        return "2021102"
