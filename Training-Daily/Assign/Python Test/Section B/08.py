#Q8) Create a Python function that takes two lists as input and returns True if they have at least one common element, False otherwise.
def have_common_element(list1, list2):
    set1 = set(list1)
    for element in list2:
        if element in set1:
            return True
    return False

list1 = [int(element) for element in input("Enter elements for Integer list 1: ").split()]
list2 = [int(element) for element in input("Enter elements for Integer list 1: ").split()]
result = have_common_element(list1, list2)
print(f"Original list : \nList 1 : {list1} \nList 2 : {list2} \nOutput: {result}")