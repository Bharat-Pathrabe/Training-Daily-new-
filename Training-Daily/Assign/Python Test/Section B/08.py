#Q8) Create a Python function that takes two lists as input and returns True if they have at least one common element, False otherwise.
def have_common_element(list1, list2):
    set1 = set(list1)
    for element in list2:
        if element in set1:
            return True
    return False

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
result = have_common_element(list1, list2)
print("Output:", result)