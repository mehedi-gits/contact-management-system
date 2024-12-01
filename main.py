from add_contact import add_contact
from view_contact import view_contacts
from search_contact import search_contact
from remove_contact import remove_contact
from contact_functions import load_existing_contacts, contact_list

load_existing_contacts()

while True:
    print('''
1. Add Contact
2. View Contact 
3. Search Contact
4. Remove Contact
0. Exit from the system.
        ''')
    option = input("Select any options: ")

    if option == '1':
        add_contact(contact_list)
    elif option == '2':
        view_contacts(contact_list)
    elif option == '3':
        search_contact(contact_list)
    elif option == '4':
        remove_contact(contact_list)
    elif option == '0':
        break
    else:
        print("Wrong choice, input the correct choice")