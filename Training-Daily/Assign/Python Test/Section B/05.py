#Q5) Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3
def count_letters_digits(sentence):
    letters_count = 0
    digits_count = 0
    for char in sentence:
        if char.isalpha():
            letters_count += 1
        elif char.isdigit():
            digits_count += 1
    return letters_count, digits_count

sentence = input("Enter a sentence: ")
letters_count, digits_count = count_letters_digits(sentence)
print("LETTERS", letters_count)
print("DIGITS", digits_count)