import abc
from book.book_info import BookInfo


class ParseStrategy(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def parse(self):
        return BookInfo()
