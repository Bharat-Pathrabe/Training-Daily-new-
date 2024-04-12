# Write a function using regular expression that validates passwords according to the requirements below and returns True if all the criteria are satisfied, and False otherwise.
# Should have at least one number.
# Should have at least one uppercase character.
# Should have at least one lowercase character.
# Should have at least one special symbol from: @ $ ! % * # ? &
# Length should be between 8 to 15 characters.

import re
pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,15}$"
password = input("Enter your password: ")
regex = re.compile(pattern)
if regex.match(password):
    print("Password is valid.")
else:
    print("Password is invalid.")
