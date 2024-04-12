# Consider we have two sets. Write a Python program for the following.
# Find the intersection of the sets.
# Find the union of the sets.
# Find the maximum value from the union of the sets.
# Find the minimum value from the union of the sets.
# Find the length of the union of the sets.

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
inter = set1.intersection(set2)
uni = set1.union(set2)
print(f" Intersection : {inter} \n Union : {uni} \n Maximum : {max(uni)} \n Minimum : {min(uni)} \n Lenght: {len(uni)}")