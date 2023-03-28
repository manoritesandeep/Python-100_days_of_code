def format_name(first_name:str, last_name:str):
    """
    Take a first and last name and format it to return
    the title case version of the input name.
    """
    if first_name == "" or last_name == "":
        return "You did not provide valid inputs."
    f_name = first_name.title()
    l_name = last_name.title()
    return f"Result: {f_name} {l_name}"

format_name(first_name=input("Enter your first name: "),
            last_name = input("Enter your last name: "))