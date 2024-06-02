class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name:-> {self.name}, Phone:-> {self.phone}, Email:-> {self.email}, Address:-> {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print(f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the book.")
        else:
            for i, contact in enumerate(self.contacts):
                print(f"{i}. Name:-> {contact.name}, Phone:-> {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if results:
            for contact in results:
                print(contact)
        else:
            print("No matching contacts found.")

    def update_contact(self, index, name, phone, email, address):
        if 0 <= index < len(self.contacts):
            self.contacts[index].name = name
            self.contacts[index].phone = phone
            self.contacts[index].email = email
            self.contacts[index].address = address
            print(f"Contact {index} updated.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            removed_contact = self.contacts.pop(index)
            print(f"Contact '{removed_contact.name}' deleted.")
        else:
            print("Invalid contact index.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book:")
        print("1. Add Contact:")
        print("2. View Contacts:")
        print("3. Search Contact:")
        print("4. Update Contact:")
        print("5. Delete Contact:")
        print("6. Exit:")

        choice = input("\nEnter your choice:-> ")

        if choice == '1':
            name = input("Enter name:-> ")
            phone = input("Enter phone number:-> ")
            email = input("Enter email:-> ")
            address = input("Enter address:-> ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search:-> ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            try:
                index = int(input("Enter contact index:-> "))
                name = input("Enter new name:-> ")
                phone = input("Enter new phone number:-> ")
                email = input("Enter new email:-> ")
                address = input("Enter new address:-> ")
                contact_book.update_contact(index, name, phone, email, address)
            except ValueError:
                print("Invalid input. Please enter a valid contact index.")
        elif choice == '5':
            try:
                index = int(input("Enter contact index: "))
                contact_book.delete_contact(index)
            except ValueError:
                print("Invalid input. Please enter a valid contact index.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
