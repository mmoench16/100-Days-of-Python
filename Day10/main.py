# Functions with Outputs

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."

    full_name = f_name.title() + " " + l_name.title()
    return full_name

print(format_name("martIn", "MoenCH"))