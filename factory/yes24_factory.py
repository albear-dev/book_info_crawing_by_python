from sites.site_info import SiteInfo
from page.page_info import PageInfo
from type.site_type import SiteType
from type.rank_type import RankType
from strategy.yes24_parse_strategy import *

class Yes24Factory:
    def __init__(self):
        pass

    __fetch_size = 200
    __fetch_key = "FetchSize"

    __url = "http://www.yes24.com"
    __url_total = __url + "/24/category/bestsellerExcel?CategoryNumber=001&sumgb=06&FetchSize="+str(__fetch_size)
    __url_monthly = __url + "/24/category/bestsellerExcel?CategoryNumber=001&sumgb=09&FetchSize="+str(__fetch_size)
    __url_weekly = __url + "/24/category/bestsellerExcel?CategoryNumber=001&sumgb=08&FetchSize="+str(__fetch_size)
    __url_daily = __url + "/24/category/bestsellerExcel?CategoryNumber=001&sumgb=07&FetchSize="+str(__fetch_size)

    def create_site_info(self):
        _site_info = SiteInfo(SiteType.YES24)
        _site_info.add_page(PageInfo(RankType.TOTAL, self.__url_total, self.__fetch_key, self.__fetch_size, Yes24ParseStrategy()))
        _site_info.add_page(PageInfo(RankType.MONTHLY, self.__url_monthly, self.__fetch_key, self.__fetch_size, Yes24ParseStrategy()))
        _site_info.add_page(PageInfo(RankType.WEEKLY, self.__url_weekly, self.__fetch_key, self.__fetch_size, Yes24ParseStrategy()))
        _site_info.add_page(PageInfo(RankType.DAILY, self.__url_daily, self.__fetch_key, self.__fetch_size, Yes24ParseStrategy()))
        return _site_info
