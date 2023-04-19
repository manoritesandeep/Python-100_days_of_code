# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random as r

names = ["Alex", "Beth", "Carolina", "Eve", "Freddie"]

student_scores = {student: r.randint(1, 100) for student in names}
print(student_scores)

# print(student_scores['Alex']>60)
# passed_students = {student: score for (student, score) in student_scores.items() if student_scores[student] >= 60}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)
