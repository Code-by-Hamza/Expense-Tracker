from datetime import datetime
import json

file = "expenses.json"

#load file 
def load_file():
    try:
        with open(file,"r") as f:
            return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        return []

#save file 
def save_file(expenses):
    with open(file,"w") as f:
        json.dump(expenses,f,indent=4)

#menu
def menu():
    print("\n---MAIN MENU---")
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. View Summary")
    print("4. Delete Expense")
    print("5. Search for a category")
    print("6. Save & Exit")

#add expenses
def add(expenses):
    while True:
        try:
            amount = int(input("Enter amount:"))
            break
        except ValueError:
            print("Invalid Number! Please Enter digits")

    category = input("Enter Category:").lower().strip()
    now = datetime.now().strftime("%B %d, %Y")
    new = {"category": category,
            "amount": amount,
            "date": now}
    expenses.append(new)

#delete espenses
def delete(expenses):
    if not expenses:
        print("No Expense to Delete!")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} - {expense['amount']}")

    while True:
        try:
            choice = int(input("Enter the Number you wish to Delete:  "))
            if 1 <= choice <= len(expenses):
                removed = expenses.pop(choice - 1)
                print(f"Deleted: {removed['category']} - {removed['amount']}")
                break
            else:
                print(f"Please Enter a Valid Digit between 1 and {len(expenses)}.")
        except ValueError:
            print("Enter a Digit Please!")

#search expenses 
def search(expenses):
    select = input("Search by Category: ").lower().strip()
    result = [expense for expense in expenses if select == expenses['category']]

    if result:
        print(f"\n---Results for {select}:---")
        for i,expense in enumerate(result,start=1):
            print(f"{i}. Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}")
            subtotal += expense['amount']
        print(f"\n---Subtotal: {subtotal}")
    else:
        print(f"{select} is not present in expenses!")


#view all expenses 
def view(expenses):
    if not expenses:
        print("List is empty")
        return
    total = 0
    for i, expense in enumerate(expenses, start=1):
            print(f"{i}. Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}")
            total += expense['amount']
    print(f"\n---Total so far: {total}---")


# summary / analyze
def analyze(expenses):
    if expenses:
        amounts = [expense['amount'] for expense in expenses]
        total = sum(amounts)
        highest = max(amounts)
        average = round(total / len(amounts), 2)
        return (f"\n-Summary-\n Total: {total}\n"
                f"Average per Expense: {average}\n"
                f"Highest Expense: {highest}\n")
    else:
        return "List is Empty!"

#main loop
def main():
    expenses = load_file()
    while True:
        menu()
        choice = input("Choose a Number:  ").lower().strip()

        if choice == "1":
            add(expenses)
            print("Added Successfully!")
        elif choice == "2":
            print("Current Expenses:")
            view(expenses)
        elif choice == "3":
            print(analyze(expenses))
        elif choice == "4":
            delete(expenses)
        elif choice == "5":
            search(expenses)
        elif choice == "6":
            save_file(expenses)
            print("Save Successfully! GoodBye!")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__" :
    main()