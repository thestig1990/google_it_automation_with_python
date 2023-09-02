import csv

# read_employees(). This function receives a CSV file as a parameter
# and returns a list of dictionaries from that file.
# my version of the feature
def read_employees(csv_file_location):
    with open(csv_file_location, "r") as filename:
        csv.register_dialect("empDialect", skipinitialspace=True, strict=True)
        employee_file = csv.DictReader(filename, dialect="empDialect")
        return list(employee_file)
        

employee_list = read_employees("employees.csv")


# lab version of the feature
# def read_employees(csv_file_location):
#     csv.register_dialect("empDialect", skipinitialspace=True, strict=True)
#     employee_file = csv.DictReader(open(csv_file_location), dialect="empDialect")
#     employee_list = []
#     for data in employee_file:
#         employee_list.append(data)
#     return employee_list
        

# employee_list = read_employees("employees.csv")


# This function needs to pass the employee_list, received from the previous section,
# as a parameter to the function.
def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

dictionary = process_data(employee_list)


# This function writes a dictionary of department: amount to a file.
# The report should have the format:
# <department1>: <amount1>
# <department2>: <amount2>
def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ": " + str(dictionary[k]) + "\n")

write_report(dictionary, "report.txt")
