# # FileNotFoundError
#
# with open("abc.txt", "r") as f:
#     f.readlines()

# # KeyError
# d = {"key":"value"}
# val = d["nope"]

# # IndexError
# ls = ["Apple", "Mango"]
# faal = ls[3]

# # TypeError
# text = "abc"
# print(text + 5)

"""
try: Something that might cause an exception
except: Do this if there was an exception
else: Do this if there was NO exception
finally: Do this no matter what happens
"""

try:
    file = open("abc.txt")
    a_dict = {"key":"value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("abc.txt","w")
    file.write("something something by mika")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("The file was closed!")












