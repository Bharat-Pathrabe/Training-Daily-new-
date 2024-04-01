#Q1) Write python program to find the second largest number in the integer list.
def second_largest(numbers):
    numbers.sort(reverse=True)
    return numbers[1]
integer_list = [10, 5, 20, 15, 30]
print("Second largest number:", second_largest(integer_list))