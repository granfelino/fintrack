from fintrack.expense import ExpenseList, Expense, Category
import pytest
import datetime as dt

TEST_AMOUNT = 100.0
TEST_CAT    = Category.FOOD
TEST_DESC   = "Weekly grocery shopping."
TEST_DATE   = dt.date(2025, 6, 10)

@pytest.fixture
def exp():
    return Expense(TEST_AMOUNT,
                   TEST_CAT,
                   TEST_DESC,
                   TEST_DATE)

@pytest.fixture
def exp_list():
    return ExpenseList()

def test_expense_attr(exp):
    assert exp.amount == TEST_AMOUNT
    assert exp.category == TEST_CAT
    assert exp.desc == TEST_DESC
    assert exp.date == TEST_DATE

def test_expense_date_opt():
    Expense(TEST_AMOUNT,
                   TEST_CAT,
                   TEST_DESC)

def test_expense_wrong_vals():
    with pytest.raises(ValueError):
        Expense(-200,
                TEST_CAT,
                TEST_DESC,
                TEST_DATE)

def test_expense_list():
    ExpenseList()

def test_expense_list_add(exp, exp_list):
    exp_list.add(exp)
    assert next(x for x in exp_list.list) == exp

def test_expense_list_to_json(exp_list):
    result = exp_list.to_json()
    assert isinstance(result["list"], list[str])

def test_expense_list_to_csv():
    assert False
