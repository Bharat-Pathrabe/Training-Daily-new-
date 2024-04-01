#Q2) Write a Python program to count the frequency of each element in a list.
#Example:
#Input: nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
#Output: {1:2, 2:3, 3:2, 4:2, 5:1}
def count_frequency(nums):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
frequency = count_frequency(nums)
print("Output:", frequency)