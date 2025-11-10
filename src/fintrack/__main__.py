from fintrack.expense import Expense, ExpenseList
import datetime as dt
import pathlib as pl

def print_options() -> None:
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

def _input_date() -> dt.date:
    while True:
        try:
            y, m, d = input("Enter each after space - year, month, day: ").split()
        except ValueError:
            print("Give all 3 at the same time.")
        else:
            break

    y = int(y)
    m = int(m)
    d = int(d)

    ret = None
    try:
        ret = dt.date(y, m, d)
    except ValueError:
        print("Invalid date given.")
        return ret

    return ret

def input_add_expense(exp: ExpenseList) -> None:
    amt = float(input("Enter amount: "))
    if amt < 0:
        print("Amount cannot be negative.")
        return

    cat = input("Enter category (rent, food, health, lifestyle, savings, leisure): ")
    cat = ExpenseList.str_to_cat(cat)
    if cat is None:
        return

    desc = input("Enter description: ")

    date = None
    want_date = None
    while want_date != "y" and want_date != "n":
        want_date = input("Do you want to add a date? (y/n) ")
        print(want_date)

    if want_date == "y":
        date = _input_date()
        if date is None:
            return

    exp.add(Expense(amt, cat, desc, date))

def input_expense_by_date(exp: ExpenseList) -> None:
    print("Date FROM")
    f = _input_date()

    print("Date TO")
    t = _input_date()

    if t < f:
        print("TO is an earlier date than FROM")
        return

    exp.view_by_date(f, t)

def input_expense_by_cat(exp: ExpenseList) -> None:
    cat = input("Enter category (rent, food, health, lifestyle, savings, leisure): ")
    cat = ExpenseList.str_to_cat(cat)
    if cat is None:
        return
    exp.view_cat(cat)

def input_to_json(exp: ExpenseList) -> None:
    path = input("Store path (to a JSON file): ")
    exp.to_json(pl.Path(path))

def input_load_json() -> ExpenseList:
    print("Warning: this will overwrite the current expense list.")
    exp = None
    path = input("Enter a path to the JSON file of expenses: ")
    exp = ExpenseList.from_json(pl.Path(path))
    if exp is None:
        exp = ExpenseList()
        print("Failed to load.")
    return exp

def input_to_csv(exp: ExpenseList) -> None:
    path = input("Store path (to a CSV file): ")
    exp.to_csv(pl.Path(path))

def input_load_csv() -> ExpenseList:
    print("Warning: this will overwrite the current expense list.")
    exp = None
    path = input("Enter a path to the CSV file of expenses: ")
    exp = ExpenseList.from_csv(pl.Path(path))
    if exp is None:
        exp = ExpenseList()
        print("Failed to load.")
    return exp

def main() -> None:
    exp = ExpenseList()
    while True:
        print_options()
        choice = int(input("Enter option number: "))

        match choice:
            case 1:
                input_add_expense(exp)
            case 2:
                exp.view_all()
            case 3:
                input_expense_by_date(exp)
            case 4:
                input_expense_by_cat(exp)
            case 5:
                exp.summary_by_cat()
            case 6:
                input_to_json(exp)
            case 7:
                input_to_csv(exp)
            case 8:
                exp = input_load_json()
            case 9:
                exp = input_load_csv()
            case 10:
                exit()

if __name__ == "__main__":
    main()
