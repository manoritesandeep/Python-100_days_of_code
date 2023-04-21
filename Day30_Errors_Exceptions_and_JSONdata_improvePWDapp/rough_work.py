import json

# Add error handling

# try:
#     data_file = open("data.json", "r"):
#         # Reading the data
#         data = json.load(data_file)
#         # Updating old data with new data
#         data.update(new_data)
#
# except FileNotFoundError:
#     data_file = open('data.json',"w")
#     json.dump(data, data_file, indent=4)
#
# else:
#     # Save updated data
#     with open("data.json", "w") as data_file:
#         json.dump(data, data_file, indent=4)
#         # Clear fields once data is added
#         website_entry.delete(0, END)
#         password_entry.delete(0, END)

user_input = "google"   # This value will be taken from the uhmmm... entry box for website...
try:
    with open("demo_data.json", "r") as f:
        data = json.load(f)
        print(type(data))
except FileNotFoundError:
    # Add messagebox "No Data File Found"
    print("remove this print after adding messagebox")
else:
    for i in data.keys():
        # print(i)
        if i == user_input.lower():
            # Add messagebox here...
            print(data[user_input]["password"])
            break
    else:
        # Add messagebox "No details for the website exist"
        print("Oops, wrong val for website")
    # print(data["google"])


"""
an exception is something that is meant to be exceptional. 
It's something that happens very rarely. Whereas if and else catches things that happen frequently.
"""




