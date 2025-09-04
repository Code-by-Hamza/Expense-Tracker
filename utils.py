import json,os,csv
from datetime import datetime 

#menu
def menu():
    print("\n-----MAIN MENU-----")
    print("1. ➡ Add Expense")
    print("2. ➡ Delete Expense")
    print("3. ➡ Edit Expense")
    print("4. ➡ Undo Last Action")
    print("5. ➡ Search for a category")
    print("6. ➡ View all Expenses")
    print("7. ➡ Monthly Report")
    print("8. ➡ View Summary")
    print("9. ➡ View Category wise Summary")
    print("10. ➡ Export Expenses as CSV File")
    print("11.➡ Import Expenses from CSV File")
    print("12.➡ Save & Exit")

#load file 
def load_file(file="expenses.json"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, file)
    
    try:
        with open(filepath,"r") as f:
            return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        return []

#save file 
def save_file(expenses, file="expenses.json"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, file)
    with open(filepath,"w") as f:
        json.dump(expenses,f,indent=4)
    print("✔ Saved Successfully! GoodBye!👋")

#undo file 
undo_file = "undo.json"
#undo load
def load_undofile():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir,undo_file)
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r") as f:
        return json.load(f)
#undo save
def save_undofile(action):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, undo_file)
    with open(filepath, "w") as f:
        json.dump(action, f)
#undo clear
def clear_undofile():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir,undo_file)
    if os.path.exists(filepath):
        os.remove(filepath)

#undo last action
last_action = {}
def undo_action(expenses):
    last_action = load_undofile()
    if not last_action:
        print("No action to Undo!")
        return
    
    if last_action['type'] == 'delete':
        expenses.insert(last_action['index'],last_action['expense'])
        print("✔Undo Successful! Restored deleted expense.")
    elif last_action['type'] == 'edit':
        expenses[last_action['index']] = last_action['expense']
        print("✔Undo Successful! Reverted edited expense.")
    elif last_action['type'] == 'add':
        expenses.pop()
        print("✔Undo Successful! Deleted Added Expense.")

    clear_undofile()





#add expenses
def add(expenses):
    while True:
        category = input("Enter Category:").lower().strip()
        if category.isalpha() and len(category) >= 3:
            break
        else:
            print("❌Invalid! Only Letters allowed, minimum three characters.")
    
    while True:
        try:
            amount = int(input("Enter amount:  "))
            break
        except ValueError:
            print("❌ Invalid Number! Please Enter digits")
    now = datetime.now().strftime("%a,%b %#d,%y")
    new = {"category": category,
            "amount": amount,
            "date": now}
    expenses.append(new)
    save_undofile({
            'type': 'add',
            'index': len(expenses) - 1,
            'expense': new
                })
    print("✔ Added Successfully!")

#delete espenses
def delete(expenses):
    if not expenses:
        print("No Expense to Delete!💨")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}.{expense['date']}  -{expense['category']:<7} -{expense['amount']}")

    while True:
        try:
            choice = int(input("Enter the Number you wish to Delete:  "))
            if 1 <= choice <= len(expenses):
                removed = expenses.pop(choice - 1)
                print(f"Deleted: {removed['category']} - {removed['amount']}")
                save_undofile({
                    'type': 'delete',
                    'index': choice - 1,
                    'expense': removed
                })
                break
            else:
                print(f"❌Please Enter a Valid Digit between 1 and {len(expenses)}.")
        except ValueError:
            print("❌Enter a Digit Please")

#search expenses 
def search(expenses):
    select = input("🔎Search by Category: ").lower().strip()
    result = [expense for expense in expenses if select == expense['category']]

    if result:
        print(f"\n-----Results for {select}:-----")
        for i,expense in enumerate(result,start=1):
            print(f"{i}. {expense['date']:<14} {expense['category']:<10}Amount: {expense['amount']:<10}")
            subtotal = 0
            subtotal += expense['amount']
        print(f"\n-----💲Subtotal: {subtotal}-----")
    else:
        print(f"❌{select} is not present in expenses!")


#view all expenses 
def view(expenses):
    if not expenses:
        print("List is empty💨")
        return
    #sort by date
    sorted_expenses = sorted(expenses, key=lambda x: datetime.strptime(x['date'], "%a,%b %#d,%y"),reverse=True)
    
    total = 0
    print("💲Current Expenses: (Sorted by Date)\n")
    print(f"{'#':<3} {'Date':<14} {'Category':<15} {'Amount':<10}")
    print(f"-" * 45)

    for i, expense in enumerate(sorted_expenses, start=1):
            print(f"{i}.  {expense['date']:<14} {expense['category']:<15}{expense['amount']:<10}")
            total += expense['amount']
    print(f"\n-----💲Total so far: {total}-----")


#summary
def summary(expenses):
    if not expenses:
        print("Nothing to Summarize T-T")
        return
    amounts = [expense['amount'] for expense in expenses]
    total = sum(amounts)
    highest = max(amounts)
    average = round(total / len(amounts), 2)
    print(f"\n      -----Summary-----\n💲Total Expense:{' ':<7}{total}\n"
        f"💲Average per Expense: {average}\n"
        f"💲Highest Expense:{' ':<5}{highest}\n")


#category summary
def category_summary(expenses):
    if not expenses:
        print("Nothing to Summarize T-T")
        return
    summary = {}
    for expense in expenses:
        cat = expense['category']
        amt = expense['amount']
        if cat not in summary:
            summary[cat] = []
        summary[cat].append(amt)
    
    grand_total = sum(sum(amounts) for amounts in summary.values())
    for i, (cat, amounts) in enumerate(summary.items(), start=1):
        total = sum(amounts)
        average = total / len(amounts)
        highest = max(amounts)
        percent = (total/grand_total) * 100
        print(f"\n{i}. {cat} ({percent:.2f}%)")
        print(f"➡ Total: {total}")
        print(f"➡ Average: {average:.2f}")
        print(f"➡ Highest: {highest}")
        print(f"➡ Expenses Details: {', '.join(map(str, amounts))}")


#edit expenses
def edit_expenses(expenses):
    if not expenses:
        print("No Expenses to Edit")
        return

    for i,expense in enumerate(expenses,start=1):
        print(f"{i}. {expense['category']:<10}:  💲{expense['amount']:<5} ➡ {expense['date']}")

    while True:
        try:
            choice = int(input("Choose a Number to Edit:"))
            if 1 <= choice <= len(expenses):
                break
            else:
                print(f"❌Invalid Choice! Enter a digit from 1 to {len(expenses)}")
        except ValueError:
            print("❌Invalid Choice! Please enter a Number")

    expense = expenses[choice - 1]
    old_expense = expense.copy()

    new_cat = input(f"Enter New Category\n(Leave blank to keep {expense['category']}):  ")
    new_amt = input(f"Enter New Amount\n(Leave blank to keep {expense['amount']}):  ")
    new_date = input(f"Enter New Date\n(Leave blank to keep {expense['date']}):  ")
    
    if new_cat:
        expense['category'] = new_cat
    if new_amt:
        try:
            expense['amount'] = float(new_amt)
        except ValueError:
            print("❌Invalid Choice! Keeping the old Value")
    if new_date:
        expense['date'] = new_date
    save_undofile({
            'type': 'edit',
            'index': choice - 1,
            'expense': old_expense
            })
    print("Expense Edited ✔Successfully!")

#export in csv
def export_to_csv(expenses,filename="expenses.csv"):
    if not expenses:
        print("No Expenses to Export!")
        return

    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    with open(filepath, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount'])
        writer.writeheader()
        writer.writerows(expenses)

    print(f"Expenses exported ✔Successfully! Filename = '{filepath}'")

#import from csv
def import_csv(expenses, filename="expenses.csv"):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(script_dir, filename)
        with open(filepath,mode="r") as f:
            reader = csv.DictReader(f)
            for row in reader :
                expense = {
                    "category": row["category"].lower().strip(),
                    "amount": int(row["amount"]),
                    "date": row["date"]
                }
                if expense not in expenses:
                    expenses.append(expense)
        print(f"Imported expenses from {filename} successfuly!")
    except FileNotFoundError:
        print(f"{filename} not Found!")
    except Exception as e:
        print(f"Error importing from {filename}: {e}")

#monthly report
def monthly_report(expenses):
    if not expenses:
        print("No Expenses Found!")
        return
    user_input = input("Enter Month and Year:(eg. aug 25)  ").strip()
    try:
        target_date = datetime.strptime(user_input,"%b %y")
    except ValueError:
        print("Invalid Format! Please use 'Month YY'(eg. aug 25)")
        return
    filtered = []
    for expense in expenses:
        exp_date = datetime.strptime(expense['date'],"%a,%b %#d,%y")
        if exp_date.month == target_date.month and exp_date.year == target_date.year:
            filtered.append(expense)
    if not filtered:
        print(f"No Expenses Found for {user_input}.")
        return
    
    print("\n----Expenses----")
    for i,expense in enumerate(expenses,start=1):
        print(f"{i}. {expense['date']:<14}{expense['category']:<13}{expense['amount']:<10}")
    
    amount = [exp['amount'] for exp in filtered]
    total = sum(amount)
    highest = max(amount)
    average = total / len(amount)

    print("\n---Summary---")
    print(f"Total: {total}")
    print(f"Highest: {highest}")
    print(f"Average: {average:2f}")