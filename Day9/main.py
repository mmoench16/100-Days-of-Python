programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from a dictionary.
print(programming_dictionary["Bug"])

# Adding new items to a dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Create an existing dictionary
empty_dict = {}

# Wipe a dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Looping trough dictionaries
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Munich", "Berlin", "Hannover"],
}

print(travel_log["France"])

# Nesting a dictionary in a dictionary
extended_travel_log = {
    "France": {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Munich", "Berlin", "Hannover"], "sausages_eaten": 6},
}

print(extended_travel_log["France"])

# Nesting a dictionary in a list
list_travel_log = [
    {
        "country": "France", "cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits": 12
    },
    {
        "country": "Germany", "cities_visited": ["Munich", "Berlin", "Hannover"], "sausages_eaten": 6
    },
]