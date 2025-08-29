# Expense Tracker

A simple command-line expense tracker written in Python. This tool allows you to add, view, search, delete, and analyze your expenses, storing all data in a local JSON file.

## Features
- **Add Expense:** Enter amount and category to log a new expense.
- **View Expenses:** Display all recorded expenses with totals.
- **View Summary:** See total, average, and highest expense.
- **Delete Expense:** Remove an expense by selecting its number.
- **Search by Category:** Find expenses by category and see subtotals.
- **Save & Exit:** Save all changes to `expenses.json` and exit.

## How It Works
- Expenses are stored in `expenses.json` in the project root.
- The program uses a simple menu-driven interface.
- All amounts are entered as integers.

## Usage
1. Run the script:
   ```powershell
   python expence_tracker.py
   ```
2. Follow the on-screen menu to manage your expenses.

## Requirements
- Python 3.x

## File Structure
- `expence_tracker.py`: Main script.
- `expenses.json`: Data file (created automatically).

## Example
```
---MAIN MENU---
1. Add Expense
2. View all Expenses
3. View Summary
4. Delete Expense
5. Search for a category
6. Save & Exit
```

## License
This project is for personal use and learning purposes.
