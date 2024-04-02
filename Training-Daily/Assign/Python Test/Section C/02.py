"""Q2) Create a Python class named "DictOperations" with methods to manipulate dictionaries, including:
(a) Adding a key-value pair to the dictionary.
(b) Removing a key-value pair from the dictionary.
(c) Updating the value associated with a specific key.
(d) Checking if a key exists in the dictionary.
(e) Retrieving all keys or values from the dictionary. """

class DictOperations:
    def __init__(self):
        self.dict = {}
    
    def add_key_value(self,key,value):
        self.dict[key] = value
        print("\nKey-Value pair added Successfully")

    def remove_key_value(self,key):
        if key in self.dict:
            del self.dict[key]
            print("\nKey-Value pair removed Successfully")
        else:
            print("\nKey-Value pair not found")
    
    def update_key_value(self,key):
        if key in self.dict:
            new_value=input(f"\nEnter new value for {key}: ")
            self.dict[key] = new_value
            print(f"\nThe key {key} successfully updated")
        else:
            print("\nRequested key not found")
    
    def check_key_value(self,key):
        if key in self.dict:
            print(f"\nRequested key exist")
        else:
            print("\nRequested key does not exist")

    def retrieve_key(self):
        return list(self.dict.keys())
    
    def retrieve_value(self):
        return list(self.dict.values())

dict_oper=DictOperations()
while True:
    print("""
    1. Add a key-value pair"
    2. Remove a key-value pair"
    3. Update the value associated with a key"
    4. Check if a key exists"
    5. Retrieve all keys"
    6. Retrieve all values"
    7. Exit""")

    ch=int(input("Enter your choice:"))

    match ch:
        case 1:
            key=input("Enter the key: ")
            value=input("Enter the value: ")
            dict_oper.add_key_value(key,value)

        case 2:
            key=input("Enter the key to remove: ")
            dict_oper.remove_key_value(key)

        case 3:
            key=input("Enter the key to update: ")
            dict_oper.update_key_value(key)

        case 4:
            key=input("Enter the key to check: ")
            dict_oper.check_key_value(key)

        case 5:
            print(f"All keys: {dict_oper.retrieve_key()}")

        case 6:
            print(f"All Values: {dict_oper.retrieve_value()}")

        case 7:
            print("----------Exiting Program----------")
            break

        case default:
            print("Invalid Choice! Please enter correct value.")