#Q3) Write a Python program to find the common elements between two lists.
#Example:
#Input: list_a = [1, 2, 3, 4, 5] and list_b = [4, 5, 6, 7, 8]
#Output: [4, 5]
def find_common_elements(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    common_elements = set_a.intersection(set_b)
    return list(common_elements)

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common_elements = find_common_elements(list_a, list_b)
print("Output:", common_elements)