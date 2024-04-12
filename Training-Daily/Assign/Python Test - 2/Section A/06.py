#What will be the output of the following Python code?

def additem(listParam):
    listParam += [1]
mylist = [1, 2, 3, 4]
additem(mylist)
print(len(mylist))