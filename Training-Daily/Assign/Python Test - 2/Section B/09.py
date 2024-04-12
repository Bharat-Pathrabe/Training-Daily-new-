# Write a program to print multiplication table of a given number.
# Input: num -— 2
# Output: 2 4 6 8 10 12 14 16 18 20

num = 2
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(num * i, end=" ")