#Write a function to read last n lines from a text file.
#Example: test.txt file:
#line1
#line2
#line3
#line4
#line5
#line6
#line7
#Input: read_file(test.txt, 2) Output:
#line6
#line7

file_name = "test.txt"
n = 2
file = open(file_name, 'r')
lines = file.readlines()
file.close()
last_n_lines = lines[-n:]

for line in last_n_lines:
    print(line, end='')