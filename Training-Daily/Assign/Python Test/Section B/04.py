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

word = input("Enter the word: ")
vowel_count = count_vowels(word)
print(f"Original word: {word} \nVowel count: {vowel_count}")