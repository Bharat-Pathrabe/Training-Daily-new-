#Q13) What will be the output of the following Python code?
def even_check(num):
    if num % 2 == 0:
        return True
    else:
        return False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(even_check, numbers)
print(list(even_numbers))