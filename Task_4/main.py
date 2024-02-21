from helpers import *

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        userInput = input("Enter a command: ")
        command, *args = parseInput(userInput)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(addContact(args, contacts))
        elif command == "change":
            print(updateContact(args, contacts))
        elif command == "phone":
            print(findContact(args, contacts))
        elif command == "all":
           print(getAllContacts(contacts))        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
