# Convert the following code to List Comprehension.
"""my_string = "I will score at least"
k = []
for i in my_string.lower():
    if i not in "aeiou":
        k.append(i)
print(k) """

my_string = "I will score at least"
k = [i for i in my_string.lower() if i not in "aieou"]
print(k)