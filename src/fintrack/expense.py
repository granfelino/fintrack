from enum import Enum, auto
import datetime as dt
from typing import TypedDict
import copy
import pathlib as pl
import json
import pandas as pd

class Category(Enum):
    RENT = auto()
    TRANSPORT = auto()
    FOOD = auto()
    HEALTH = auto()
    LIFESTYLE = auto()
    SAVINGS = auto()
    LEISURE = auto()

CAT_TO_STR = {
        Category.RENT : "rent",
        Category.FOOD : "food",
        Category.HEALTH : "health",
        Category.LIFESTYLE : "lifestyle",
        Category.SAVINGS : "savings",
        Category.LEISURE : "leisure"
}

STR_TO_CAT = {v : k for k, v in CAT_TO_STR.items()}

class ExpenseDict(TypedDict):
    amount: float
    category: str
    desc: str
    date: str | None

class Expense():
    def __init__(self,
                 amount: float,
                 category: Category,
                 desc: str,
                 date: dt.date | None = None):
        if amount < 0:
            raise ValueError("Amount needs to be 0 or greater.")

        self.__amount = amount
        self.__category = category
        self.__desc = desc
        self.__date = date

    def __eq__(self, new: object):
        if not isinstance(new, Expense):
            return False

        return (
                self.amount == new.amount
                and self.category == new.category
                and self.desc == new.desc
                and self.date == new.date
                )

    @classmethod
    def from_dict(cls, new: ExpenseDict):
        new_cat = STR_TO_CAT[new["category"]]
        new_date = dt.datetime.strptime(new["date"], "%Y-%m-%d").date()
        return cls(new["amount"],
                   new_cat,
                   new["desc"],
                   new_date)

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
                "category" : CAT_TO_STR[self.category],
                "desc" : self.desc,
                "date" : str(self.date)
                }

class ExpenseList():
    def __init__(self, new: list[ExpenseDict] | None = None):
        self.__list = [] if new is None else list(new)

    def __eq__(self, new: object):
        if not isinstance(new, ExpenseList):
            return False
        return self.list == new.list

    @property
    def list(self):
        return self.__list

    @classmethod
    def from_json(cls, store_path: pl.Path):
        new = None
        with open(store_path, "r") as f:
            new = json.load(f)
        new_list = [Expense.from_dict(x) for x in new["list"]]
        return cls(new_list)

    @classmethod
    def from_csv(cls, store_path: pl.Path):
        df = pd.read_csv(store_path)
        dict_list = df.to_dict(orient="records")
        return cls([Expense.from_dict(x) for x in dict_list])

    def add(self, new: Expense):
        self.list.append(copy.copy(new))

    def to_dict(self):
        return { "list" : [x.to_dict() for x in self.list] }

    def to_json(self, store_path: pl.Path):
        with open(store_path, "w") as f:
            json.dump(self.to_dict(), f)

    def to_csv(self, store_path: pl.Path):
        tmp_dict = self.to_dict()
        df = pd.DataFrame(tmp_dict["list"])
        df.to_csv(store_path, index=False)
