# raise

# try:
#     file = open("abc.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("abc.txt","w")
#     file.write("something something by mika")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is a made up error that will crash this code file")

# Raising your own errors
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height cannot exceed 3 meters")

bmi = weight / height**2
print(bmi)



