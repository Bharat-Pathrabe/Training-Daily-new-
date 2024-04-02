#Q1) Write python program to find the second largest number in the integer list.
def second_largest(integer_list):
    integer_list.sort()
    return integer_list[-2]

integer_list = [int(element) for element in input("Enter elements for Integer list: ").split()]
print(f"Original List: {integer_list} \nSecond largest number: {second_largest(integer_list)}")