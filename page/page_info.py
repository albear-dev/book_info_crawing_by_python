from type.rank_type import RankType
from strategy.parse_strategy import ParseStrategy
from type.book_store_type import BookStoreType


class PageInfo:

    def __init__(self, rank_type: RankType, url: str, fetch_var_name: str, fetch_size: int, parse_strategy: ParseStrategy):
        self.rank_type = rank_type
        self.url = url
        self.fetch_var_name = fetch_var_name
        self.fetch_size = fetch_size
        self.parse_strategy = parse_strategy
        self.book_info_collection = list()
