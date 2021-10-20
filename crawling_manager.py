import requests
from type.site_type import SiteType
from factory.site_factory import SiteFactory
from sites.site_info import SiteInfo
from excel.excel_handler import ExcelHandler
from crawling_page_manager import CrawlingPageManager
from crlogging.cr_logger import CRLogger
import threading
import crlogging
import time


class CrawlingManager:
    workers = list()
    __logger = CRLogger.get_logger(__name__)

    @classmethod
    def start(cls, fn_update_callback, file_path, file_name):
        cls.__logger.debug("Start CrawlingManager!")
        excel_handler = ExcelHandler(file_path, file_name)

        # site별 worker 생성
        for site_type in SiteType:
            worker_name = "worker-crawling-"+site_type.name
            t = Worker("worker-crawling-"+site_type.name, lambda: cls.crowling(worker_name, SiteFactory.create(site_type), excel_handler))  # sub thread 생성
            cls.workers.append(t)
            t.start()  # sub thread의 run 메서드를 호출

    @classmethod
    def stop(cls):
        for t in cls.workers:
            t.stop()

    @classmethod
    def crowling(cls, worker_name: str, site_info: SiteInfo, excel_handler):
        is_stopped = False
        for page in site_info.pages:
            if is_stopped:
                break

            for t in cls.workers:
                #cls.__logger.debug("Thread name[%s] Worker name[%s] is stopped[%s]", t.name, worker_name, t.stopped())
                if t.name == worker_name and t.stopped():
                    cls.__logger.debug("Do break!")
                    is_stopped = True
                    break

            cls.__logger.info("Start crowling page [%s][%s]", site_info.site_type, page.rank_type)
            page.book_info_collection = CrawlingPageManager.crowling_page(page)
            page.title = site_info.site_type.desc + " " + page.rank_type.desc
            excel_handler.add_page(page)
            cls.__logger.info("End crowling page [%s][%s]", site_info.site_type, page.rank_type)

        #excel_handler.create()

class Worker(threading.Thread):
    __logger = CRLogger.get_logger(__name__)

    def __init__(self, name, fn_run):
        super(Worker, self).__init__()
        self._stop = threading.Event()
        self.name = name  # thread 이름 지정
        self.fn_run = fn_run

    def stop(self):
        self.__logger.info("Receive thread stop command.")
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def run(self):
        self.fn_run()
