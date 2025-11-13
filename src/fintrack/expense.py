from enum import Enum, auto
import datetime as dt
from typing import TypedDict, cast
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
        new_date = dt.datetime.strptime(str(new["date"]), "%Y-%m-%d").date()
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
    def date(self) -> dt.date | None:
        return self.__date

    def to_dict(self) -> ExpenseDict:
        return {
                "amount" : self.amount,
                "category" : CAT_TO_STR[self.category],
                "desc" : self.desc,
                "date" : str(self.date)
                }

class ExpenseList():
    def __init__(self, new: list[Expense] | None = None):
        self.__list = [] if new is None else list(new)

    def __eq__(self, new: object):
        if not isinstance(new, ExpenseList):
            return False
        return self.exp_list == new.exp_list

    @property
    def exp_list(self) -> list[Expense]:
        return self.__list

    @classmethod
    def from_json(cls, store_path: pl.Path):
        if not store_path.exists():
            print(f"Path {store_path} does not exists.")
            return None

        if not store_path.suffix == ".json":
            print(f"Path {store_path} does not point to a JSON file.")
            return None

        new = None
        with open(store_path, "r") as f:
            new = json.load(f)

        if "exp_list" not in new.keys():
            print("Invalid JSON contents.")
            return None

        new_list = [Expense.from_dict(x) for x in new["exp_list"]]
        return cls(new_list)

    @classmethod
    def from_csv(cls, store_path: pl.Path):
        if not store_path.exists():
            print(f"Path {store_path} does not exists.")
            return None

        if not store_path.suffix == ".csv":
            print(f"Path {store_path} does not point to a CSV file.")
            return None

        df = pd.read_csv(store_path)
        if set(df.columns) != {"amount", "date", "desc", "category"}:
            print("Invalid CSV contents.")
            return None

        dict_list = df.to_dict(orient="records")
        tmp_list = [Expense.from_dict(cast(ExpenseDict, x)) for x in dict_list]
        return cls(tmp_list)

    def add(self, new: Expense) -> None:
        self.exp_list.append(copy.copy(new))

    def to_dict(self) -> dict[str, list[ExpenseDict]]:
        return { "exp_list" : [x.to_dict() for x in self.exp_list] }

    def to_json(self, store_path: pl.Path) -> None:
        if not store_path.exists():
            print(f"Path {store_path} does not exist.")
            return

        if not store_path.is_dir():
            print(f"Path {store_path} does not point to a directory.")
            return 

        store_path = store_path / "exp.json"
        if store_path.exists():
            print("File already exists. Aborting.")

        with open(store_path, "w") as f:
            json.dump(self.to_dict(), f)

    def to_csv(self, store_path: pl.Path) -> None:
        if not store_path.exists():
            print(f"Path {store_path} does not exist.")
            return

        if not store_path.is_dir():
            print(f"Path {store_path} does not point to a directory.")
            return 

        store_path = store_path / "exp.csv"
        if store_path.exists():
            print("File already exists. Aborting.")

        tmp_dict = self.to_dict()
        df = pd.DataFrame(tmp_dict["exp_list"])
        df.to_csv(store_path, index=False)

    def _to_df(self) -> pd.DataFrame:
        tmp_dict = self.to_dict()
        tmp_list = tmp_dict["exp_list"]
        if not tmp_list:
            return pd.DataFrame(columns=["amount", "category", "desc", "date"])

        df = pd.DataFrame(tmp_list)
        df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d", errors="coerce")
        return df

    def _total_expenses(self) -> float:
        df = self._to_df()
        return sum(df["amount"])

    def _print_total_expenses(self) -> None:
        print(f"Total expenses: {self._total_expenses()}")

    def view_all(self) -> None:
        print(self._to_df())
        self._print_total_expenses()

    def __sum_expenses(self, df: pd.DataFrame) -> float:
        return sum(df["amount"])

    def view_cat(self, cat: Category) -> None:
        df = self._to_df()
        cat_str = CAT_TO_STR[cat]
        df = df[df["category"] == cat_str]
        exp = self.__sum_expenses(df)
        print(df)
        print(f"Expenses on {cat_str}: {exp}")

    def view_by_date(self, f: dt.date, t: dt.date) -> None:
        df = self._to_df()
        f_pd = pd.to_datetime(f)
        t_pd = pd.to_datetime(t)
        df = df[(df["date"] >= f_pd) & (df["date"] <= t_pd)]
        exp = self.__sum_expenses(df)
        print(df)
        print(f"Expenses between {f} and {t}: {exp}")

    def summary_by_cat(self):
        df = self._to_df()
        tmp_map = {c : 0 for c in CAT_TO_STR.values()}
        for c in tmp_map.keys():
            df_tmp = df[df["category"] == c]
            tmp_map[c] = self.__sum_expenses(df_tmp)

        print("Summary of expenses by category:")
        for c, e in tmp_map.items():
            print(f"{c}: {e}")

    @staticmethod
    def cat_to_str(c: Category):
        return CAT_TO_STR[c]

    @staticmethod
    def str_to_cat(c: str):
        if c not in STR_TO_CAT.keys():
            print("Invalid category.")
            return None
        return STR_TO_CAT[c]
