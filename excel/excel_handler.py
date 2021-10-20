from openpyxl import Workbook
from page.page_info import PageInfo
import os
from queue import Queue
import threading
from crlogging.cr_logger import CRLogger

class ExcelHandler:
    __logger = CRLogger.get_logger(__name__)

    def __init__(self, path, filename):
        self.page_processing_queue = Queue()
        self.write_wb = Workbook()
        self.path = path
        self.filename = filename
        self.worker = threading.Thread(target=self.excel_write)
        self.worker.start()
        #self.worker.join()

    def add_page(self, page: PageInfo):
        self.page_processing_queue.put(page)

    def excel_write(self):
        while True:
            page = self.page_processing_queue.get()
            self.__logger.info("get page object [%s]", page)

            if not page:
                break

            self.__logger.info("Start excel write page [%s]", page.title)

            # create workbook
            write_ws = self.write_wb.create_sheet(page.title)
            self.__logger.info("Sheet created [%s]", page.title)

            # write title
            write_ws.append(["순위", "상품번호", "상품명", "정가", "할인가", "출판사", "저자", "출간일", "판매지수"])
            for data in page.book_info_collection:
                # write data
                write_ws.append([
                    data.rank,
                    data.prod_no,
                    data.prod_nm,
                    data.price,
                    data.sale_price,
                    data.publisher,
                    data.author,
                    data.release_date,
                    data.selling_score
                ])
            self.__logger.info("Finish write data to sheet [%s] count[%d]", page.title, len(page.book_info_collection))

        save_path = os.path.join(self.path, self.filename)
        self.write_wb.save(save_path)
        self.__logger.info("Excel file save done. [%s]", save_path)
