student_dict = {
    "students":["Dave", "Jeff", "Elon"],
    "grades": [55, 75, 85]
}

# # Looping through dictionaries
# for key, value in student_dict.items():
#     print(key)
#     print(value)

import pandas as pd

student_df = pd.DataFrame(data=student_dict)
# print(student_df)

# Loop through df.. this does it on column rather than rows so not really useful
# for (key, value) in student_df.items():
#     print(value)

# iterrows() - allows us to loop through each of the rows of the data frame rather than each of the columns.
# loop through rows of a df
for (index, row) in student_df.iterrows():
    # print(row.students)
    # print(row.grades)
    if row.students == "Dave":
        print(row.grades)
        break
    else:
        print("Oops, Student not found!")
