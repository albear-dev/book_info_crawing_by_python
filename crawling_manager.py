import requests
from type.site_type import SiteType
from factory.site_factory import SiteFactory
from sites.site_info import SiteInfo
from excel.excel_handler import ExcelHandler
from crawling_page_manager import CrawlingPageManager
from crlogging.cr_logger import CRLogger
import threading
import concurrent.futures


class CrawlingManager:
    workers = list()
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    __logger = CRLogger.get_logger(__name__)

    @classmethod
    def start(cls, fn_update_callback, file_path, file_name):
        cls.__logger.debug("Start CrawlingManager!")
        excel_handler = ExcelHandler(file_path, file_name)

        # site별 worker 생성
        for site_type in SiteType:
            cls.crowling(SiteFactory.create(site_type), excel_handler)

    @classmethod
    def stop(cls):
        #for t in cls.workers:
        #    t.stop()
        pass

    @classmethod
    def crowling(cls, site: SiteInfo, excel_handler):
        for page in site.pages:
            crawling_page_manager = CrawlingPageManager()
            cls.__logger.info("Start crowling page [%s][%s]", site.site_type, page.rank_type)
            cls.workers.append(cls.pool.submit(crawling_page_manager.crowling_page, site, page))

        for future in concurrent.futures.as_completed(cls.workers):
            page = future.result()
            cls.__logger.info("End crowling page [%s][%s]", site.site_type, page.rank_type)
            excel_handler.add_page(future.result())
