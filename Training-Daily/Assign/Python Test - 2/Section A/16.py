# In the following Python code, which function is the decorator?
def mk(x):
    def mk1():
        print("Decorated")
    x()
    return mk1

def mk2():
    print("Ordinary")

p = mk(mk2)


# answer - def mk(x)
