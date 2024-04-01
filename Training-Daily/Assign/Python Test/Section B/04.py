#Q4) Write a Python program to count Vowels in a Given Word.
#Example:
#Input: word = "programming"
#Output: 3
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

word = "programming"
vowel_count = count_vowels(word)
print("Output:", vowel_count)