from data import parse_input
from processing import add_contact,change_number, show_phone, show_all

def main():
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

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
            show_all(contacts)
        else:
            print('Invalid command')

if __name__ == '__main__':
    main()