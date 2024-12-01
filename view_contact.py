from contact_functions import contact_list

def view_contacts(contact_list):
    for contact in contact_list:
        print(f"Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']} | Address: {contact['address']}")