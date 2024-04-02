"""Q1) Write a Python function that takes a list of dictionaries representing students' grades (keys: 'name' and 'grade') and returns a dictionary where the keys are the grade levels ('A', 'B', 'C') and the values are the counts of students who received each grade.
Example:
Input: dict1 = [{"name": "Maulik", "grade": "A"}, {"name": "Jignesh", "grade": "A"}, {"name": "Arjun", "grade": "B"}, {"name": "Hemin", "grade": "C"}]
Output: {"A":2, "B": 1, "C": 1}""" 
def get_grades_from_input():
    student_grades=[]
    while True:
        name=input("Enter name of student(or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        grade=input(f"Enter the grade for {name}: ").upper()
        student_grades.append({"Name":name,"Grade":grade})
    return student_grades

def grade_count(user_list_dict):
    grade_count = {}
    for student in user_list_dict:
        grade = student["Grade"] 
        if grade in grade_count:
            grade_count[grade] += 1
        else:
            grade_count[grade] = 1
    return grade_count

user_list_dict=get_grades_from_input()
grade_count=grade_count(user_list_dict)
print(f"List entered by user: {user_list_dict} \nGrade count: {grade_count}")