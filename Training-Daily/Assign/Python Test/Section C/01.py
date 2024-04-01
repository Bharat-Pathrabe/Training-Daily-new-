"""Q1) Write a Python function that takes a list of dictionaries representing students' grades (keys: 'name' and 'grade') and returns a dictionary where the keys are the grade levels ('A', 'B', 'C') and the values are the counts of students who received each grade.
Example:
Input: dict1 = [{"name": "Maulik", "grade": "A"}, {"name": "Jignesh", "grade": "A"}, {"name": "Arjun", "grade": "B"}, {"name": "Hemin", "grade": "C"}]
Output: {"A":2, "B": 1, "C": 1}""" 
def count_grades(students):
    grade_count = {'A': 0, 'B': 0, 'C': 0}
    for student in students:
        grade = student['grade']
        grade_count[grade] += 1
    return grade_count

dict1 = [
    {"name": "Maulik", "grade": "A"},
    {"name": "Jignesh", "grade": "A"},
    {"name": "Arjun", "grade": "B"},
    {"name": "Hemin", "grade": "C"}
]
grades_count = count_grades(dict1)
print("Output:", grades_count)