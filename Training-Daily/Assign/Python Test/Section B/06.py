#Q6) Create a Python function that takes two dictionaries as input and merges them into a single dictionary. If there are any common keys, the #values should be added together.
#Example:
#Input: dict1 = {"a":1, "b": 2}, dict2 = {"c":3, "a":4}
#Output: {"a":5, "b": 2, "c":3}
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "a": 4}
merged_dict = merge_dictionaries(dict1, dict2)
print("Output:", merged_dict)