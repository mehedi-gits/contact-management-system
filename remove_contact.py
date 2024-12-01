from contact_functions import contact_list

def remove_contact(contact_list):

    for sl, contact in enumerate(contact_list):
        print(f"{sl + 1}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")

    select_contact = int(input("Enter the contact SL no you want to remove: ")) - 1

    contact_list.pop(select_contact)

    with open("contacts.csv", "w") as fp:
        for contact in contact_list:
            line = f"{contact['name']}, {contact['phone']}, {contact['email']}, {contact['address']}\n"
            fp.write(line)

    print("Contact removed successfully.")