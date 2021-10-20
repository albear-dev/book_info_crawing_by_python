from enum import Enum


class BookStoreType(Enum):
    YES24 = (1, "예스24")
    KYOBO = (2, "교보")
    ALADIN = (3, "알라딘")

    def __init__(self, idx, desc):
        self.idx = idx
        self.desc = desc

