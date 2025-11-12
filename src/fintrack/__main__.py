from fintrack.expense import Expense, ExpenseList
from fintrack.cli import *
import logging

logging.basicConfig(
        filename="expense_tracker.log",
        filemode="w",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
        )

def main() -> None:
    logging.info("Application started.")

    exp = ExpenseList()
    while True:
        print_options()
        choice = int(input("Enter option number: "))

        match choice:
            case 1:
                logging.info(f"Choice {choice} - adding expense.")
                input_add_expense(exp)
            case 2:
                logging.info(f"Choice {choice} - view all.")
                exp.view_all()
            case 3:
                logging.info(f"Choice {choice} - filtering by date.")
                input_expense_by_date(exp)
            case 4:
                logging.info(f"Choice {choice} - filtering by category.")
                input_expense_by_cat(exp)
            case 5:
                logging.info(f"Choice {choice} - summary by category.")
                exp.summary_by_cat()
            case 6:
                logging.info(f"Choice {choice} - to JSON.")
                input_to_json(exp)
            case 7:
                logging.info(f"Choice {choice} - to CSV.")
                input_to_csv(exp)
            case 8:
                logging.info(f"Choice {choice} - loading from JSON.")
                exp = input_load_json()
            case 9:
                logging.info(f"Choice {choice} - loading from CSV.")
                exp = input_load_csv()
            case 10:
                logging.info(f"Choice {choice} - exit.")
                exit()

if __name__ == "__main__":
    main()
