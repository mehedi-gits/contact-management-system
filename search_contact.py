from contact_functions import contact_list

def search_contact(contact_list):
    search_term = input("Enter Search Term: ").lower()

    matches_found = False

    for contact in contact_list:

        if (search_term in contact['name'].lower() or
                search_term in contact['phone'].lower() or
                search_term in contact['email'].lower() or
                search_term in contact['address'].lower()):
            print(f"Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']} | Address: {contact['address']}")
            matches_found = True
    if not matches_found:
        print("No contacts found!")