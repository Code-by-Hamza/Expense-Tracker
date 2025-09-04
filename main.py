from utils import load_file,menu,add,delete,search,view,analyze,undo_action,monthly_report
from utils import category_summary,save_file,edit_expenses,export_to_csv,import_csv
#main loop
def main():
    expenses = load_file()
    while True:
        menu()
        choice = input("\n➡ Choose a Option:  ").lower().strip()

        if choice == "1":
            add(expenses)
        elif choice == "2":
            delete(expenses)
        elif choice == "3":
            edit_expenses(expenses)
        elif choice == "4":
            undo_action(expenses)
        elif choice == "5":
            search(expenses)
        elif choice == "6":
            view(expenses)
        elif choice == "7":
            monthly_report(expenses)
        elif choice == "8":
            print(analyze(expenses))
        elif choice == "9":
            category_summary(expenses)
        elif choice == "10":
            export_to_csv(expenses)
        elif choice == "11":
            import_csv(expenses)
        elif choice == "12":
            save_file(expenses)
            break
        else:
            print("Invalid❌ Choice! Try again!")

if __name__ == "__main__" :
    main()
