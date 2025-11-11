from fintrack.expense import Expense, ExpenseList
from fintrack.cli import *

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
