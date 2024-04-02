#Q6) Create a Python function that takes two dictionaries as input and merges them into a single dictionary. If there are any common keys, the #values should be added together.
#Example:
#Input: dict1 = {"a":1, "b": 2}, dict2 = {"c":3, "a":4}
#Output: {"a":5, "b": 2, "c":3}
def get_dictionary_from_input(x):
    dictionary = {}
    while True:
        key = input(f"Dict{x}: Enter a key (or type 'done' to finish): ")
        if key.lower() == 'done':
            break
        value = int(input(f"Dict{x}: Enter the value for '{key}': "))
        dictionary[key] = value
    return dictionary

def merge_dictionaries(user_dict,user_dict2):
    merged_dict= user_dict.copy()
    for key,value in user_dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

user_dict = get_dictionary_from_input(1)
user_dict2= get_dictionary_from_input(2)
merged_dict=merge_dictionaries(user_dict,user_dict2)
print(f"Dictionary entered by the user:\nDict 1: {user_dict}\nDict 2: {user_dict2}")
print(f"Merged Dictionary: {merged_dict}")