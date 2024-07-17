names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_names = [name.upper() for name in names if len(name) >= 5]
print(new_names)