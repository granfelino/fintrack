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

def test_expense_eq(exp):
    tmp_exp = Expense(TEST_AMOUNT,
                   TEST_CAT,
                   TEST_DESC,
                   TEST_DATE)
    assert exp == tmp_exp

def test_expense_to_dict(exp):
    result = exp.to_dict()
    keys = result.keys()
    assert (isinstance(result, dict)
            and "amount" in keys 
            and "category" in keys
            and "desc" in keys
            and "date" in keys
            )

def test_expense_from_dict(exp):
    expected = exp.to_dict()
    actual = Expense.from_dict(expected)
    assert actual == exp

def test_expense_list():
    ExpenseList()

def test_expense_list_add(exp, exp_list):
    exp_list.add(exp)
    assert next(x for x in exp_list.list) == exp

def test_expense_list_to_dict(exp_list):
    result = exp_list.to_dict()
    assert isinstance(result, dict)
    assert "list" in result.keys()

def test_expense_list_to_json(exp, exp_list, tmp_path):
    exp_list.add(exp)
    store_path = tmp_path
    exp_list.to_json(store_path)
    store_path = store_path / "exp.json"
    assert store_path.exists()
    assert store_path.is_file()

def test_expense_list_to_csv(exp, exp_list, tmp_path):
    store_path = tmp_path / "exp.csv"
    exp_list.add(exp)
    exp_list.to_csv(tmp_path)
    assert store_path.exists()
    assert store_path.is_file()
    assert store_path.suffix == ".csv"

def test_expense_list_eq(exp, exp_list):
    exp_list.add(exp)
    tmp_list = ExpenseList([exp])
    assert tmp_list == exp_list

def test_expense_list_from_json(exp, exp_list, tmp_path):
    exp_list.add(exp)
    store_path = tmp_path
    exp_list.to_json(store_path)
    result = ExpenseList.from_json(store_path / "exp.json")
    assert exp_list == result

def test_expense_list_from_csv(exp, exp_list, tmp_path):
    exp_list.add(exp)
    store_path = tmp_path / "exp.csv"
    exp_list.to_csv(tmp_path)
    result = ExpenseList.from_csv(store_path)
    assert exp_list == result

def test_view_all(exp, exp_list):
    exp_list.add(exp)
    exp_list.view_all()

def test_view_cat(exp, exp_list):
    exp_list.add(exp)
    exp_list.view_cat(Category.FOOD)

def test_view_by_date(exp, exp_list):
    exp_list.add(exp)
    exp_list.view_by_date(dt.date(2025, 1, 10), dt.date(2025, 2, 10))

def test_summary_by_cat(exp, exp_list):
    exp_list.add(exp)
    exp_list.summary_by_cat()
