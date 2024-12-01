from contact_functions import contact_list

def add_contact(contact_list):

    while True:
        name = input("Enter Name: ")
        if isinstance(name, str) and len(name) > 0:
            break
        else:
            print("Invalid name entry, name can not be empty.")

    while True:
        phone = input("Enter Mobile Number: ")
        if phone.isdigit():
            if any(contact['phone'] == phone for contact in contact_list):
                print(f"The phone number {phone} already exists!")
            else:
                break
        else:
            print(f"Invalid phone number: {phone}. It must contain only digits.")

    while True:
        email = input("Enter Email ID: ")
        if '@' in email:
            break
        else:
            print(f"Invalid email: {email}.")

    while True:
        address = input("Enter Address: ")
        if len(address) > 0:
            break
        else:
            print("Invalid address entry. Address cannot be empty.")

    contact = {'name': name, 'phone': phone, 'email': email, 'address': address}

    with open('contacts.csv', 'a', newline='') as fp:

        line = f"{contact['name']}, {contact['phone']}, {contact['email']}, {contact['address']}\n"
        fp.write(line)
    
    contact_list.append(contact)

    print("Contact added successfully!")