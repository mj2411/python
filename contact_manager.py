def contact_manager():
    contacts = {}  

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            contacts[name] = phone
            print(f"Contact {name} added successfully!")

        elif choice == '2':
            name = input("Enter name to search: ")
           
            result = contacts.get(name, "Contact not found.")
            print(f"Result: {result}")

        elif choice == '3':
            if not contacts:
                print("The contact book is empty.")
            else:
                print("\nAll Contacts:")
                for name, phone in contacts.items():
                    print(f"Name: {name} | Phone: {phone}")

        elif choice == '4':
            name = input("Enter name to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"{name} deleted.")
            else:
                print("Name not found.")

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_manager()