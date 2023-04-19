"""
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
You are going to create a list called result which contains the numbers that are common in both files.
"""

with open('file1.txt') as f:
    num1 = f.readlines()
    # print(num1)

with open('file2.txt') as f:
    num2 = f.readlines()
    # print(num2)

# ls = []
# for num in num1:
#     for n in num2:
#         if num == n:
#             ls.append(int(num))
# print(sorted(list(set(ls))))


# result = [new_item for item in list if test]
result = [int(num) for num in num1 if num in num2]

# Write your code above 👆

print(result)


