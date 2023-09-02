import csv

users = [
    {"name": "Sol Mansi", "username": "solm", "department": "IT Infrastructure"},
    {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
    {"name": "Charlie Grey", "username": "greyc", "department": "Development"},
]

keys = ["name", "username", "department"]

with open("by_department.csv", "w", newline="") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)


# class csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)
# Create an object which operates like a regular writer but maps dictionaries onto output rows. 
# The fieldnames parameter is a sequence of keys that identify the order in which values in the 
# dictionary passed to the writerow() method are written to file f. The optional restval parameter
# specifies the value to be written if the dictionary is missing a key in fieldnames. If the dictionary
# passed to the writerow() method contains a key not found in fieldnames, the optional extrasaction 
# parameter indicates what action to take. If it is set to 'raise', the default value, a ValueError is
# raised. If it is set to 'ignore', extra values in the dictionary are ignored. Any other optional or 
# keyword arguments are passed to the underlying writer instance.

# !!!!!!!! Note that unlike the DictReader class, the fieldnames parameter of the DictWriter class is not optional !!!!!!!!!!!!!!!!    

# print(dir(csv))
# print(help(csv))
# print(help(csv.DictWriter))

