# ✅ **Project Requirements — Expense Tracker (CLI)**

## 1. **Project Overview**

The Expense Tracker is a command-line application that allows users to record, view, and manage personal expenses. The program must support persistent storage through JSON and CSV files, maintain an audit trail via logging, and include automated tests using `pytest`.

---

# ✅ **Functional Requirements**

## 2. **Core CLI Features**

### **2.1 Add Expense**

The application must allow the user to add a new expense with the following fields:

* **amount** (float; required)
* **category** (string; required)
* **description** (string; optional)
* **date** (string; optional; defaults to today in `YYYY-MM-DD` format)

**Behavior:**

* Input validation must be enforced (e.g., amount must be numeric and positive).
* New expenses must be appended to the in-memory list and persisted to the default storage file when saved.

---

### **2.2 View Expenses**

The program must support viewing expenses in multiple ways:

* **View all expenses**
* **Filter by category**
* **Filter by date**
* **Show total expenses**

**Output requirements:**

* Displayed in a readable, tabular-like text layout.
* Summaries (e.g., totals per category) must be formatted cleanly.

---

### **2.3 Data Persistence**

The program must support saving and loading data in two formats:

#### **JSON Format**

* Must save the complete list of expenses in a `.json` file.
* Must correctly load existing data at startup (if file exists).

#### **CSV Format**

* Must support exporting expenses into a `.csv` file.
* Must support importing data from CSV (optional but recommended).

---

### **2.4 CLI Menu**

The program must implement an interactive menu such as:

1. Add expense
2. View expenses
3. Save to JSON
4. Save to CSV
5. Exit

* Must run until the user explicitly exits.
* Must handle invalid menu selections gracefully.

---

# ✅ **Non-Functional Requirements**

## 3. **Logging Requirements**

The application must use the built-in `logging` module.

### **3.1 Logging Levels**

* `INFO` — successful operations (e.g., "Expense added")
* `WARNING` — invalid input or recoverable issues
* `ERROR` — failures such as file read/write errors
* `DEBUG` — internal details for development and testing

### **3.2 Log Output**

* Logs must be written to a file named `expense_tracker.log`.
* The log format must include timestamp, level, and message.

---

## 4. **Testing Requirements**

### **4.1 Testing Framework**

* All tests must use **pytest**.

### **4.2 Unit Tests Must Cover:**

* Adding an expense:

  * valid inputs
  * invalid inputs (e.g., negative amount)
* Viewing/filtering logic
* JSON serialization & deserialization
* CSV export functionality
* Error handling (e.g., missing file)
* Logging calls (optional but recommended)

### **4.3 Test Quality Requirements**

* Tests must be isolated (avoid using production files).
* Use `tmp_path` for temporary file operations.
* Use mocks where appropriate (e.g., for logging or input).

---

# ✅ **Architecture & Code Requirements**

## 5. **Project Structure**

Recommended minimum structure:

```
expense_tracker/
│── tracker.py              # Core logic
│── cli.py                  # User interface & menu loop
│── storage_json.py         # JSON handling
│── storage_csv.py          # CSV handling
│── logger_config.py        # Logging setup
│── tests/
│   ├── test_add_expense.py
│   ├── test_storage_json.py
│   ├── test_storage_csv.py
│   └── test_view.py
│── expenses.json           # Auto-created if missing
│── requirements.txt
```

---

## 6. **Code Quality Requirements**

* Follow PEP 8 formatting.
* Use type hints for all functions.
* Use docstrings describing arguments, return values, and behavior.
* Functions must be pure where possible (I/O separated from logic).
* Error handling should be robust and descriptive.

---
