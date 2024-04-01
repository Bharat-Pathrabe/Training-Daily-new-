#Q7) Create a Python function that takes a dictionary as input and returns a new dictionary with keys as values and values as keys (assuming values are unique).
def swap_keys_values(input_dict):
    return {value: key for key, value in input_dict.items()}

input_dict = {"a": 1, "b": 2, "c": 3}
swapped_dict = swap_keys_values(input_dict)
print("Output:", swapped_dict)