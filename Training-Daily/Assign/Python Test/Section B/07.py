#Q7) Create a Python function that takes a dictionary as input and returns a new dictionary with keys as values and values as keys (assuming values are unique).
def get_dictionary_from_input():
    user_dict = {}
    while True:
        key = input("Enter a key (or enter 'done' to finish): ")
        if key.lower() == 'done':
            break
        value = input(f"Enter the value for {key}: ")
        user_dict[key] = value
    return user_dict

def change_dict(user_dict):
    exchanged_dict = {}
    for key,value in user_dict.items():
        exchanged_dict[value] = key
    return exchanged_dict

user_dict=get_dictionary_from_input()
exchanged_dict=change_dict(user_dict)
print(f"Dictionary entered by the user: {user_dict} \nExchanged Keys and values dictionary: {exchanged_dict}")