# Expense Tracker

A simple command-line expense tracker written in Python. This tool allows you to add, view (Sorted by date), search, delete, undo last action, summarize your expenses, summarize by category,edit expenses,create a csv file and storing all data in a local JSON file.

## Features
- **Add Expense:** Enter amount and category to log a new expense.
- **Delete Expense:** Remove an expense by selecting its number.
- **Edit Expenses** Edit existing Expenses.
- **Undo last action** Undo the previous change.
- **Search by Category:** Find expenses by category and see subtotals.
- **View Expenses:** Display all recorded expenses with totals.
- **View Summary:** See total, average, and highest expense.
- **Category Summary** See total category wise.
- **Export as CSV** Create a .csv file that can be exported.
- **Save & Exit:** Save all changes to `expenses.json` and exit.

## How It Works
- Expenses are stored in `expenses.json` in the project root.
- The program uses a simple menu-driven interface.
- All amounts are entered as integers.

## Usage
1. Run the script:
   ```powershell
   python main.py
   ```
2. Follow the on-screen menu to manage your expenses.

3. You can also open the folder in code editors like VScode.

## Requirements
- Python 3.10+

## File Structure
- `main.py`: Main script.
- `utils.py` : All features.
- `expenses.json`: Data file (created automatically).
- `expenses.csv` : CSV file for exporting.

## Example
```
---MAIN MENU---
1. Add Expense
2. Delete Expense
3. Edit Expense
4. Undo Last Action
5. Search for a category
6. View all Expenses (Sorted by date)
7. View Summary
8. View Category wise Summary
9. Export Expenses as CSV
10. Save & Exit
~~~
