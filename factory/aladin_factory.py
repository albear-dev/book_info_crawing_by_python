from sites.site_info import SiteInfo
from page.page_info import PageInfo
from type.site_type import SiteType
from type.rank_type import RankType
from type.book_store_type import BookStoreType
from strategy.aladin_parse_strategy import AladinParseStrategy

class AladinFactory:
    def __init__(self):
        pass

    __fetch_size = 200
    __fetch_key = "FetchSize"

    __url = "https://www.aladin.co.kr"
    __url_weekly = __url + "/shop/common/wbest_excel.aspx?BestType=Bestseller&BranchType=1&CID=0&Year=2021&Month=10&Week=3"
    __url_daily = __url + "/shop/common/wbest_excel.aspx?BestType=DailyBest&BranchType=1&CID=0"

    def create_site_info(self):
        _site_info = SiteInfo(SiteType.ALADIN)
        _site_info.add_page(PageInfo(RankType.WEEKLY, self.__url_weekly, self.__fetch_key, self.__fetch_size, AladinParseStrategy()))
        _site_info.add_page(PageInfo(RankType.DAILY, self.__url_daily, self.__fetch_key, self.__fetch_size, AladinParseStrategy()))
        return _site_info
