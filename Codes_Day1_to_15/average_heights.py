"""
You are going to write a program that calculates the average student height 
    from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the
    heights together and dividing by the total number of heights.
"""

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
# student_heights = [180, 124, 165, 173, 189, 169, 146]
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# avg_heights = sum(student_heights)/len(student_heights)
# print(round(avg_heights))


##### OR using for loops #####
total_height = 0
for height in student_heights:
  total_height += height
print(total_height)

num_of_students = 0
for student in student_heights:
  num_of_students += 1
print(num_of_students)

print(f"Avg. height = {round(total_height/num_of_students)}")
























