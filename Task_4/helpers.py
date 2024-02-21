def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such name found"
        except IndexError:
            return "Enter user name"
        except Exception as e:
            return f"Error: {e}" 

    return inner

@input_error
def parseInput(userInput):
    cmd, *args = userInput.split()
    cmd = cmd.strip().lower()
    return cmd, *args
@input_error
def addContact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return 'Contact added'
    else:
        return "Contact already exists"
@input_error   
def updateContact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated"
    else:
        # raise KeyError
        return f"Contact with name {name} not found"
@input_error    
def findContact(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        # raise KeyError
        return f"Contact with name {name} not found" 
@input_error   
def getAllContacts(contacts):
    if len(contacts) > 0:
        return contacts
    else:
        return "Contacts list is empty"  
