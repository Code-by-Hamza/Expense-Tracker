
# Expense Tracker

A simple command-line expense tracker written in Python. This tool lets you add, view (sorted by date), search, delete, edit, undo last action, view monthly reports, summarize your expenses, view category summaries, export your data to CSV, and import expenses from CSV. All data is stored locally in JSON and CSV files.

## Features
- **Add Expense:** Log a new expense with category and amount.
- **Delete Expense:** Remove an expense by selecting its number.
- **Edit Expense:** Update category, amount, or date for any expense.
- **Undo Last Action:** Undo your previous add, edit, or delete (persistent across runs).
- **Search by Category:** Find expenses by category and see subtotals.
- **View Expenses:** Display all expenses sorted by date, with totals.
- **View Summary:** See total, average, and highest expense.
- **Category Summary:** View totals for each category.
- **Monthly Reports** View Expenses and Summary of the selected month.
- **Export as CSV File:** Export all expenses to a CSV file in the project folder.
- **Import Expenses from CSV File:** Import expenses from a CSV file into your tracker.
- **Save & Exit:** Save all changes to `expenses.json` and exit.


## How It Works
- Expenses are stored in `expenses.json` in the project folder.
- Undo actions are saved in `undo.json` for persistent undo.
- CSV exports and imports are handled in the same folder as the script.
- The program uses a menu-driven interface in the terminal.
- All amounts are entered as integers (editing allows float).

## Usage
1. Run the script:
   ```powershell
   python main.py
   ```
2. Follow the menu to manage your expenses.
3. You can also open the folder in VS Code or any code editor.

## Requirements
- Python 3.10+


## File Structure
- `main.py`: Main script and entry point.
- `utils.py`: All features and logic.
- `expenses.json`: Data file (created automatically).
- `undo.json`: Stores last action for undo (persistent).
- `expenses.csv`: CSV file for exporting and importing expenses.

## Example Menu
```
-----MAIN MENU-----
1. ➡ Add Expense
2. ➡ Delete Expense
3. ➡ Edit Expense
4. ➡ Undo Last Action
5. ➡ Search for a category
6. ➡ View all Expenses
7. ➡ Monthly Report
8. ➡ View Summary
9. ➡ View Category wise Summary
10. ➡ Export Expenses as CSV File
11.➡ Import Expenses from CSV File
12.➡ Save & Exit
```
