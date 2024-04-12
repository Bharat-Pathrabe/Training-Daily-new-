# Given a list of numbers, write a Python program to create a list of tuples having the first element as the number and the second element as the cube of the number.
# Example:
# Input: list —— [1, 2, 3]
# Output: (1, 1), (2, 8), (3, 27)]

list1 = [1,2,3]
list2 = []
for i in list1:
    list2.append((i,i**3))
print(list2)