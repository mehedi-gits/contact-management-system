contact_list = []

def load_existing_contacts():
    global contact_list

    contact_list.clear()
    try:
        with open('contacts.csv', 'r') as fp:
            for line in fp.readlines():
                split_line = line.strip().split(",")
                contact = {
                    'name': split_line[0].strip(),
                    'phone': split_line[1].strip(),
                    'email': split_line[2].strip(),
                    'address': split_line[3].strip()
                }
                contact_list.append(contact)
    except FileNotFoundError:
        pass