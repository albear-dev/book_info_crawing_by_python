import requests
from page.page_info import PageInfo
from bs4 import BeautifulSoup
from crlogging.cr_logger import CRLogger


class CrawlingPageManager:
    __logger = CRLogger.get_logger(__name__)

    def crowling_page(self, site, page):
        self.__logger.debug('Processing [%s/%s] Call URL [%s]', site.site_type, page.rank_type, page.url)

        response = requests.get(page.url)

        if response.status_code == 200:
            page.book_info_collection = page.parse_strategy.parse(BeautifulSoup(response.text, 'html.parser'))
            page.title = site.site_type.desc + " " + page.rank_type.desc
            return page
        else:
            self.__logger.error('HTTP Response ERROR! [%s]', response.status_code)
