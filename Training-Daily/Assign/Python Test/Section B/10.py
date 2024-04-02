#Q10) Write a program to address the following scenario - Given an integer list nums, return true if any value appears at least twice in the list, and return false if every element is distinct.
#Example 1:
#Input: nums = [1,2,3,1]
#Output: true
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False

nums1 = [int(element) for element in input("Enter elements for Integer list 1: ").split()]
print(f"Original list: {nums1} \nOutput: {contains_duplicate(nums1)}")