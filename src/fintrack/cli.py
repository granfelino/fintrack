from fintrack.expense import Expense, ExpenseList
import datetime as dt
import pathlib as pl
import logging

logger = logging.getLogger(__name__)

def print_options() -> None:
    """Prints options for user input."""

    print()
    print("1.  Add expense")
    print("2.  View all expenses")
    print("3.  View expenses by date")
    print("4.  View expenses by category")
    print("5.  View expenses summary by category")
    print("6.  Save to JSON")
    print("7.  Save to CSV")
    print("8.  Load from JSON")
    print("9.  Load from CSV")
    print("10. Exit")
    print()

def _input_date() -> dt.date | None:
    """
    Prompts user for input and creates a date object.

    This function does not take any parameters.

    Returns
    -------
    dt.date or None
        Date created from user input or None in case of botched input values.

    Raises
    ------
    ValueError
        If:
            - not all 3 (y, m, d) are given at the same time.
            - the date constructed from user's values is invalid.
    """

    while True:
        try:
            y, m, d = input("Enter each after space - year, month, day: ").split()
        except ValueError:
            print("Give all 3 at the same time.")
        else:
            break


    ret = None
    try:
        ys = int(y)
        ms = int(m)
        ds = int(d)

        ret = dt.date(ys, ms, ds)
    except ValueError:
        print("Invalid date given.")
        return ret

    return ret

def input_add_expense(exp: ExpenseList) -> None:
    """
    Prompts user for input and adds an expense to the passed expense list.
    This function returns nothing.

    Parameters
    ----------
    exp : ExpenseList
        The list to add the new expense to.
    """

    logging.info("Adding expense.")

    try:
        amt = float(input("Enter amount: "))
    except ValueError:
        print("Enter a numeric value.")
        return

    if amt < 0:
        logging.info("Negative amount input.")
        print("Amount cannot be negative.")
        return

    cat = input("Enter category (rent, food, health, lifestyle, savings, leisure): ")
    cat = ExpenseList.str_to_cat(cat)
    if cat is None:
        logging.info("Category not found.")
        return

    desc = input("Enter description: ")

    date = None
    want_date = None
    while want_date != "y" and want_date != "n":
        want_date = input("Do you want to add a date? (y/n) ")

    if want_date == "y":
        date = _input_date()
        if date is None:
            logging.info("Invalid date input.")
            return

    exp.add(Expense(amt, cat, desc, date))
    logging.info("Expense added succesfully")

def input_expense_by_date(exp: ExpenseList) -> None:
    """
    Filters and prints expenses by date, based on user input.
    This function returns nothing.

    Parameters
    ----------
    exp : ExpenseList
        List object to filter from.
    """

    logging.info("Filtering expenses by date.")

    print("Date FROM")
    f = _input_date()
    if f is None:
        return 

    print("Date TO")
    t = _input_date()
    if t is None:
        return

    if t < f:
        print("TO is an earlier date than FROM")
        return

    exp.view_by_date(f, t)

def input_expense_by_cat(exp: ExpenseList) -> None:
    """
    Filters expenses by category provided by the user. This function
    returns nothing.

    Parameters
    ----------
    exp : ExpenseList
        List of expenses to filter.
    """

    logging.info("Filtering expenses by category.")

    cat = input("Enter category (rent, food, health, lifestyle, savings, leisure): ")
    cat = ExpenseList.str_to_cat(cat)
    if cat is None:
        return
    exp.view_cat(cat)

def input_to_json(exp: ExpenseList) -> None:
    """
    Saves the expense list to JSON, to the location provided by the user.
    This function returns nothing.

    exp : ExpenseList
        List of expenses to save.
    """

    logging.info("Saving to JSON.")

    path = input("Store path: ")
    exp.to_json(pl.Path(path))

def input_load_json() -> ExpenseList:
    """
    Loads an expense list from JSON file. Path to the file is provided
    by the user. This function takes no parameters.

    Returns
    -------
    ExpenseList
        The expense list object created from loaded JSON contents.
    """

    logging.info("Loading from JSON.")

    print("Warning: this will overwrite the current expense list.")
    exp = None
    path = input("Enter a path to the JSON file of expenses: ")
    exp = ExpenseList.from_json(pl.Path(path))
    if exp is None:
        exp = ExpenseList()
        print("Failed to load.")
        logging.info("Failed to load from JSON.")
    return exp

def input_to_csv(exp: ExpenseList) -> None:
    """
    Saves the expense list to CSV, to the location provided by the user.
    This function returns nothing.

    exp : ExpenseList
        List of expenses to save.
    """

    logging.info("Saving to CSV.")

    path = input("Store path: ")
    exp.to_csv(pl.Path(path))

def input_load_csv() -> ExpenseList:
    """
    Loads an expense list from CSV file. Path to the file is provided
    by the user. This function takes no parameters.

    Returns
    -------
    ExpenseList
        The expense list object created from loaded CSV contents.
    """

    logging.info("Loading from CSV.")

    print("Warning: this will overwrite the current expense list.")
    exp = None
    path = input("Enter a path to the CSV file of expenses: ")
    exp = ExpenseList.from_csv(pl.Path(path))
    if exp is None:
        exp = ExpenseList()
        print("Failed to load.")
        logging.info("Failed to load from CSV.")
    return exp
