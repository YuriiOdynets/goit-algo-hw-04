#Import of commands modules
from processing import add_contact,change_number, show_phone

#Function that contains main commands, greeting, exit logic and responce.
def main():
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        #removes extra spaces from input and makes all in lower register
        command, *args = user_input.split()
        command = command.strip().lower()

        if command in ['close', 'exit']:
            print('Good bye')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args,contacts))
        elif command =='change':
            print(change_number(args,contacts))
        elif command == 'phone':
            print(show_phone(args,contacts))
        elif command =='all':
            for name, phone in contacts.items():
                print(f'{name}: {phone}')
        else:
            print('Invalid command')

if __name__ == '__main__':
    main()