from fintrack.expense import Expense, Category
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

def test_expense_attr(exp):
    assert exp.amount == TEST_AMOUNT
    assert exp.category == TEST_CAT
    assert exp.desc == TEST_DESC
    assert exp.date == TEST_DATE

def test_expense_date_opt():
    pass

def test_expense_wrong_vals():
    pass
