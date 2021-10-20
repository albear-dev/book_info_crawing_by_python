from page.page_info import PageInfo
from type.site_type import SiteType


class SiteInfo:

    def __init__(self, site_type: SiteType):
        self.site_type = site_type
        self.pages = list()

    def add_page(self, page: PageInfo):
        self.pages.append(page)
