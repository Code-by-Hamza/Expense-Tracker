from utils import load_file,menu,add,delete,search,view,analyze,category_summary,save_file,edit_expenses

#main loop
def main():
    expenses = load_file()
    while True:
        menu()
        choice = input("Choose a Option:  ").lower().strip()

        if choice == "1":
            add(expenses)
        elif choice == "2":
            delete(expenses)
        elif choice == "3":
            edit_expenses(expenses)
        elif choice == "4":
            search(expenses)
        elif choice == "5":
            view(expenses)
        elif choice == "6":
            print(analyze(expenses))
        elif choice == "7":
            category_summary(expenses)
        elif choice == "8":
            save_file(expenses)
            break
        else:
            print("Invalid Choice! Try again!")

if __name__ == "__main__" :
    main()
