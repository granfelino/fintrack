from fintrack import cli
from fintrack.expense import Expense, ExpenseList, Category
import datetime as dt
import pytest

EXP_AMT = 100
EXP_CAT = Category.FOOD
EXP_DESC = "food shopping"
EXP_DATE = dt.date(2012, 12, 13)

EXP_ARGS = [EXP_AMT, EXP_CAT, EXP_DESC, EXP_DATE]


@pytest.fixture
def exp():
    exp = ExpenseList()
    exp.add(Expense(*EXP_ARGS))
    return exp

def test_input_date(monkeypatch):
    inputs = "2012 12 31"
    monkeypatch.setattr("builtins.input", lambda _: inputs)
    result = cli._input_date()
    assert result == dt.date(2012, 12, 31)

def test_input_date_invalid_args(monkeypatch):
    inputs = iter(["12 12", "2012 12 31"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = cli._input_date()
    assert result == dt.date(2012, 12, 31)

def test_input_date_invalid(monkeypatch):
    inputs = "111 111 111"
    monkeypatch.setattr("builtins.input", lambda _: inputs)
    result = cli._input_date()
    assert result is None

def test_input_add(exp, monkeypatch):
    inputs = ["100", "food", "food shopping", "y", "2012 12 13"]
    inputs = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    cli.input_add_expense(exp)

    assert len(exp.exp_list) == 2

    g = (x for x in exp.exp_list)
    first = next(g)
    second = next(g)
    assert first == second

def test_input_add_inv_amt(exp, monkeypatch):
    inputs = "-100"
    monkeypatch.setattr("builtins.input", lambda _: inputs)
    cli.input_add_expense(exp)

    assert len(exp.exp_list) == 1

def test_input_add_inv_cat(exp, monkeypatch):
    inputs = ["100", "invalid"]
    inputs = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    cli.input_add_expense(exp)

    assert len(exp.exp_list) == 1

def test_input_add_no_date(exp, monkeypatch):
    inputs = ["100", "food", "food shopping", "n"]
    inputs = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    cli.input_add_expense(exp)

    assert len(exp.exp_list) == 2

def test_input_to_json(exp, monkeypatch, tmp_path):
    monkeypatch.setattr("builtins.input", lambda _: str(tmp_path))
    cli.input_to_json(exp)  # XXX: no crash -> all good

def test_input_to_csv(exp, monkeypatch, tmp_path):
    monkeypatch.setattr("builtins.input", lambda _: str(tmp_path))
    cli.input_to_csv(exp)   # XXX: no crash -> all good


# XXX no more tests -- I won't learn much more from them and will waste time
#     I can use on other projects
