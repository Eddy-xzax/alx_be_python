def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        #prompts the user to insert the item to be added
        if choice == '1':
            item = (input("Enter the item to add: "))
            shopping_list.append(item)
            print(f"{item} has been added to the list")
            print()
            pass
        #prompts the user to insert the item to be removed
        elif choice == '2':
         if item in shopping_list:
            item = (input("Enter an item to remove: "))
            shopping_list.remove(item)
            print(f"{item} has been removed")
        # Display the shopping list
        elif choice == '3':
            print("Your shopping list:", shopping_list) 
            print()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
