#Q9) Write a Python program that reads a text file, counts the frequency of each character, and stores the counts in a dictionary where the keys are the characters and the values are the frequencies.
def count_character_frequency(file_name):
    char_frequency = {}
    with open(file_name,"r") as file:
        for line in file:
            for char in line:
                if char in char_frequency:
                    char_frequency[char] += 1
                else:
                    char_frequency[char] = 1
    return char_frequency

file_name=input("Enter file name:")
frequency_dict = count_character_frequency(file_name)
print(f"Character Frequency: {frequency_dict}")
