#Add contact function
def add_contact(args,contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'
#Change number function
def change_number(args,contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return 'Contact has been updated'
    else:
        return 'No matches found. Contact not added.'
#Function that prints requested phone number
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        phone=contacts[name]
        return(f"{name}'s phone nuber is: {phone}")
    else:
        return'Contact not found.'
#Function that prints entire contact list
def show_all(contacts):
    for name, phone in contacts.items():
        print(f'{name}: {phone}')


