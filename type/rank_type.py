from enum import Enum


class RankType(Enum):
    TOTAL = (1, "전체")
    MONTHLY = (2, "월간")
    WEEKLY = (3, "주간")
    DAILY = (4, "일간")
    IWEEKLY = (5, "인터넷 주간")
    IDAILY = (6, "인터넷 일간")
    NONE = (99, "기타")

    def __init__(self, idx, desc):
        self.idx = idx
        self.desc = desc
