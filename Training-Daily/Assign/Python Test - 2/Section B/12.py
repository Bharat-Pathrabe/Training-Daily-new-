# Write a program to filter out odd and even numbers from a list of integers using a Lambda function.
# Example:
# Input: input_list —— [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output:
# odd_num —— [1, 3, 5, 7, 9]
# even_num —— [2, 4, 6, 8, 10]

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_num = list(filter(lambda x: x % 2 != 0, input_list))
even_num = list(filter(lambda x: x % 2 == 0, input_list))

print("Odd numbers:", odd_num)
print("Even numbers:", even_num)