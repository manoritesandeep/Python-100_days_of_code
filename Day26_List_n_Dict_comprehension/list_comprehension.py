# Syntax: new_list = [new_item for item in list]
# import random

# numbers = [1, 2, 3]
# print(numbers)
#
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(f"New list is: {new_list}")
#
# # Using List comprehension
# new_new_list = [n + 1 for n in numbers]
# print(f"New new list is:{new_new_list}")
#
# string = "Sandeep"
# new_string = [v for v in string]
# print(f"New string is: {new_string}")

# nums = range(1,5)
# # print(list(nums))
# double_nums = [n**2 for n in nums]
# print(double_nums)
#
# double_nums1 = [n**2 for n in range(1, 5)]
# print(double_nums1)

# Conditional List Comprehension
# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Carolina", "Eve", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(f"short names list is: {short_names}")

upper_names = [name.upper() for name in names if len(name) > 4]
print(f"Upper above len5 are: {upper_names}")



