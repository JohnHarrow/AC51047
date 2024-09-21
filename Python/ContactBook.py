def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"No contact found with name {name}.")

def contact_book():
    contacts = {}
    while True:
        print("\nOptions:\n1. Add contact\n2. View contacts\n3. Delete contact\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid option. Please try again.")

contact_book()