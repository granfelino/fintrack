from enum import Enum, auto
import datetime as dt
from typing import TypedDict

class Category(Enum):
    RENT = auto()
    TRANSPORT = auto()
    FOOD = auto()
    HEALTH = auto()
    LIFESTYLE = auto()
    SAVINGS = auto()
    LEISURE = auto()

class ExpenseDict(TypedDict):
    amount: float
    category: str
    desc: str
    date: str

class Expense():
    def __init__(self,
                 amt: float,
                 cat: Category,
                 desc: str,
                 date: dt.date | None = None):
        if amt < 0:
            raise ValueError("Amount needs to be 0 or greater.")

        self.__amount = amt
        self.__category = cat
        self.__desc = desc
        self.__date = date

    @property
    def amount(self) -> float:
        return self.__amount

    @property
    def category(self) -> Category:
        return self.__category

    @property
    def desc(self) -> str:
        return self.__desc

    @property
    def date(self) -> dt.date:
        return self.__date

    def to_dict(self) -> TypedDict:
        return {
                "amount" : self.amount,
                "category" : self.category
                }

class ExpenseList():
    def __init__(self):
        self.__list = []

    @property
    def list(self):
        return self.__list

    def add(self, new: Expense):
        pass
