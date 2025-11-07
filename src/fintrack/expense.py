from enum import Enum, auto
import datetime as dt

class Category(Enum):
    RENT = auto()
    TRANSPORT = auto()
    FOOD = auto()
    HEALTH = auto()
    LIFESTYLE = auto()
    SAVINGS = auto()
    LEISURE = auto()


class Expense():
    def __init__(self,
                 amt: float,
                 cat: Category,
                 desc: str,
                 date: dt.date | None):
        self.amount = amt
        self.category = cat
        self.desc = desc
        self.date = date
