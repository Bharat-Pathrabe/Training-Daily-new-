"""Q2) Create a Python class named "DictOperations" with methods to manipulate dictionaries, including:
(a) Adding a key-value pair to the dictionary.
(b) Removing a key-value pair from the dictionary.
(c) Updating the value associated with a specific key.
(d) Checking if a key exists in the dictionary.
(e) Retrieving all keys or values from the dictionary. """

class DictOperations:
    def __init__(self):
        self.dictionary = {}

    def add_pair(self, key, value):
        self.dictionary[key] = value

    def remove_pair(self, key):
        if key in self.dictionary:
            del self.dictionary[key]
            print("Key-value pair removed successfully.")
        else:
            print("Key not found in the dictionary.")

    def update_value(self, key, value):
        if key in self.dictionary:
            self.dictionary[key] = value
            print("Value updated successfully.")
        else:
            print("Key not found in the dictionary.")

    def check_key(self, key):
        return key in self.dictionary

    def get_all_keys(self):
        return list(self.dictionary.keys())

    def get_all_values(self):
        return list(self.dictionary.values())


# Example usage:
dict_ops = DictOperations()

while True:
    print("\n1. Add a key-value pair")
    print("2. Remove a key-value pair")
    print("3. Update the value associated with a key")
    print("4. Check if a key exists")
    print("5. Retrieve all keys")
    print("6. Retrieve all values")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        dict_ops.add_pair(key, value)
    elif choice == '2':
        key = input("Enter the key to remove: ")
        dict_ops.remove_pair(key)
    elif choice == '3':
        key = input("Enter the key to update: ")
        value = input("Enter the new value: ")
        dict_ops.update_value(key, value)
    elif choice == '4':
        key = input("Enter the key to check: ")
        if dict_ops.check_key(key):
            print("Key exists in the dictionary.")
        else:
            print("Key does not exist in the dictionary.")
    elif choice == '5':
        print("All keys:", dict_ops.get_all_keys())
    elif choice == '6':
        print("All values:", dict_ops.get_all_values())
    elif choice == '7':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
