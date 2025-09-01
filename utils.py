import json,os,csv
from datetime import datetime 

#menu
def menu():
    print("\n---MAIN MENU---")
    print("1.➡ Add Expense")
    print("2.➡ Delete Expense")
    print("3.➡ Edit Expense")
    print("4.➡ Search for a category")
    print("5.➡ View all Expenses")
    print("6.➡ View Summary")
    print("7.➡ View Category wise Summary")
    print("8.➡ Export Expenses as CSV")
    print("9.➡ Save & Exit")

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


# summary / analyze
def analyze(expenses):
    if expenses:
        amounts = [expense['amount'] for expense in expenses]
        total = sum(amounts)
        highest = max(amounts)
        average = round(total / len(amounts), 2)
        return (f"\n-----Summary-----\n💲Total Expense:{' ':<7}{total}\n"
                f"💲Average per Expense: {average}\n"
                f"💲Highest Expense:{' ':<5}{highest}\n")
    else:
        return "List is Empty!💨"

#category summary
def category_summary(expences):
    if not expences:
        print("Nothing to Summarize T-T")
        return
    summary = {}
    for expense in expences:
        cat = expense['category']
        amt = expense['amount']
        summary[cat] = summary.get(cat,0) + amt
    
    print("\n----Category Summary----")
    for cat,total in summary.items():
        print(f"    {cat:<10}: {total}")

#edit expenses
def edit_expenses(expenses):
    if not expenses:
        print("No Expenses to Edit")
        return

    for i,expense in enumerate(expenses):
        print(f"{i}. {expense['category']:<10}:  💲{expense['amount']:<5} ➡ {expense['date']}")

    while True:
        try:
            choice = int(input("Choose a Number to Edit:"))
            if 0 <= choice < len(expenses):
                break
            else:
                print(f"Invalid Choice! Enter a digit from 0 to {len(expenses) - 1}")
        except ValueError:
            print("Invalid Choice! Please enter a Number")

    expense = expenses[choice]

    new_cat = input(f"Enter New Category\n(Leave blank to keep {expense['category']}):  ")
    new_amt = input(f"Enter New Amount\n(Leave blank to keep {expense['amount']}):  ")
    new_date = input(f"Enter New Date\n(Leave blank to keep {expense['date']}):  ")
    
    if new_cat:
        expense['category'] = new_cat
    if new_amt:
        try:
            expense['amount'] = float(new_amt)
        except ValueError:
            print("Invalid Choice! Keeping the old Value")
    if new_date:
        expense['date'] = new_date
    
    print("Expense Edited Successfully!")

#export in csv
def export_to_csv(expenses,filename="expenses.csv"):
    if not expenses:
        print("No Expenses to Export!")
        return
    
    with open(filename,mode="w",newline="") as file:
        writer = csv.DictWriter(file,fieldnames=['date','category','amount'])
        writer.writeheader()
        writer.writerows(expenses)

    print("Expenses exported Successfully! Filename = 'expenses.csv'")

