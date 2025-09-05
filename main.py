from utils import load_file,menu,add,delete,search,view,summary,undo_action,monthly_report,search_date
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
            search_date(expenses)
        elif choice == "6":
            search(expenses)
        elif choice == "7":
            view(expenses)
        elif choice == "8":
            monthly_report(expenses)
        elif choice == "9":
            summary(expenses)
        elif choice == "10":
            category_summary(expenses)
        elif choice == "11":
            export_to_csv(expenses)
        elif choice == "12":
            import_csv(expenses)
        elif choice == "13":
            save_file(expenses)
            break
        else:
            print("Invalid❌ Choice! Try again!")

if __name__ == "__main__" :
    main()
