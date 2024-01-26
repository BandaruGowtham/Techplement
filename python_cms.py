import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts, name, phone, email):
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact {name} added successfully!")

def search_contact(contacts, name):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"Contact with name {name} not found.")

def update_contact(contacts, name, phone, email):
    if name in contacts:
        contacts[name]["phone"] = phone
        contacts[name]["email"] = email
        save_contacts(contacts)
        print(f"Contact {name} updated successfully!")
    else:
        print(f"Contact with name {name} not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            add_contact(contacts, name, phone, email)
        elif choice == "2":
            name = input("Enter the name to search: ")
            search_contact(contacts, name)
        elif choice == "3":
            name = input("Enter the name to update: ")
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email address: ")
            update_contact(contacts, name, phone, email)
        elif choice == "4":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
