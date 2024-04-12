#Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list
#Example:
#Input: list1 —— [23, 65, 19, 90], pos1 —— 1, pos2 —— 3
#Output: [19, 65, 23, 90]

list1 = [23, 65, 23, 90]
pos1 = 1
pos2 = 3

temp = list1[pos1 - 1]
list1[pos1 - 1] = list1[pos2 - 1]
list1[pos2 - 1] = temp

print(list1)  