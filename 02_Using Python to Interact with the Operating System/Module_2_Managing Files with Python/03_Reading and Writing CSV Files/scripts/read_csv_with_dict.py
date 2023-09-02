import csv

with open("employees.csv") as employees:
    reader = csv.DictReader(employees)
    # print(type(reader))
    for row in reader:
        # print(row)
        print(f"Employee '{row['First Name']} {row['Last Name']}' has monthly salary {row['Salary']}$")
    

# class csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
# Create an object that operates like a regular reader but maps the information in each row to a dict
# whose keys are given by the optional fieldnames parameter.
# The fieldnames parameter is a sequence. If fieldnames is omitted, the values in the first row of file f
# will be used as the fieldnames. Regardless of how the fieldnames are determined, the dictionary preserves
# their original ordering.


# print(dir(csv))
# print(help(csv))
# print(help(csv.DictReader))

