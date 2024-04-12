# Sort Python dictionaries in ascending order by Key.
# Example:
# Input: {’ravi’: 10, ’rajnish ’: 9, ’sanjeev’: 15, ’yash ’: 2, ’suraj’: 32)
# Output: {’rajnish ’: 9, ’ravi’: 10, ’sanjeev’: 15, ’suraj’: 32, ’yash': 2}

s = {'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash ': 2}
k = dict(sorted(s.items(), key=lambda item: item[0]))
print(k)