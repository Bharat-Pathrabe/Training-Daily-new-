# We are given a string, write a program to reverse words of a given string.
# Example:
# Input: “geeks quiz practice code” 
# Oufput: “code practice quiz geeks”

str1 = input("Enter sentence: ").split()
s = " ".join(str1[::-1])
print(s)