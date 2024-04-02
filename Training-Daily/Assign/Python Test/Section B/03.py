#Q3) Write a Python program to find the common elements between two lists.
#Example:
#Input: list_a = [1, 2, 3, 4, 5] and list_b = [4, 5, 6, 7, 8]
#Output: [4, 5]
def find_common(integer_list1,integer_list2):
    set_1=set(integer_list1)
    set_2=set(integer_list2)
    common_elements=set_1.intersection(set_2)
    return list(common_elements)

integer_list1 = [int(element) for element in input("Enter elements for Integer list 1: ").split()]
integer_list2 = [int(element) for element in input("Enter elements for Integer list 2: ").split()]
common_elements=find_common(integer_list1,integer_list2)
print(f"Original list are: \nlist 1 : {integer_list1} \nlist 2 : {integer_list2} \nCommon Elements : {common_elements}")