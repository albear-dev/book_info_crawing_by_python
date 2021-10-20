from type.site_type import SiteType
from factory.yes24_factory import *
from factory.kyobo_factory import *
from factory.aladin_factory import *


class SiteFactory:
    __default_fetch_size = 200
    __default_fetch_key = "FetchSize"

    def __init__(self, site_type):
        pass

    @classmethod
    def create(cls, site_type: SiteType):
        if site_type == SiteType.YES24:
            return Yes24Factory().create_site_info()
        elif site_type == SiteType.KYOBO:
            return KyoboFactory().create_site_info()
        elif site_type == SiteType.ALADIN:
            return AladinFactory().create_site_info()
        else:
            raise Exception("Type not found!")
