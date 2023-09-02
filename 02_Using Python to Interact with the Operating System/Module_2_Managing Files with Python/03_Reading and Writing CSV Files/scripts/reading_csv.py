import csv

file = open("employees.csv")

# 'csv.reader' method - The returned object is an iterator. 
# Each iteration returns a row of the CSV file (which can span multiple input lines).
csv_file = csv.reader(file)

for row in csv_file:
    first_name, last_name, email, phone, gender, department, job_title, experience, salary = row
    print(f"Name: {first_name} {last_name}, Email: {email}, Phone: {phone}, Gender: {gender}, Department: {department}, Job Title: {job_title}, Experience: {experience} years, Salary: {salary}$")

file.close()


# print(dir(csv))
print(help(csv.reader))

