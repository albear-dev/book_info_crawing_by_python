import requests
from page.page_info import PageInfo
from bs4 import BeautifulSoup
from crlogging.cr_logger import CRLogger


class CrawlingPageManager:
    __logger = CRLogger.get_logger(__name__)

    @classmethod
    def crowling_page(cls, page: PageInfo):
            cls.__logger.debug('Call URL[%s]', page.url)
            response = requests.get(page.url)

            if response.status_code == 200:
                return page.parse_strategy.parse(BeautifulSoup(response.text, 'html.parser'))
            else:
                cls.__logger.error('HTTP Response ERROR! [%s]', response.status_code)
