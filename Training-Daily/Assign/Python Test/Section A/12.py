#Q12) Write python code to get the value of the key “apples” if it exists and returns 0 if it does not?
fruits = {'bananas': 7, 'apples': 4, 'grapes': 19, 'pears': 4}
apples_value = fruits.get('apples', 0)
print(apples_value)