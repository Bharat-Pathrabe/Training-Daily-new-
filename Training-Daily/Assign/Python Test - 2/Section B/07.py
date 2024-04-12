# Count the total number of digits in a number without converting it to a string.
# Example:
# Input: 75869

x = 75869
count = 0
while x != 0:
    x = x // 10  
    count += 1  
print(count)