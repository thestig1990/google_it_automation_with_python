#!/usr/bin/python3

# ********Log Analysis Using Regular Expressions**********
# Command 1 cat syslog.log
# Command 2 grep ticky syslog.log
# Command 3 grep "ERROR" syslog.log
# Command 4 grep "ERROR Tried to add information to closed ticket" syslog.log
# Command 5 python3
# Command 6 import re
# line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
# Comamnd 7 re.search(r"ticky: INFO: ([\w ]*) ", line)
# Comamnd 8 line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
# Comamnd 9 re.search(r"ticky: ERROR: ([\w ]*) ", line)
# Command 10 fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
# Command 11 sorted(fruit.items())
# Command 12 import operator
# Command 13 sorted(fruit.items(), key=operator.itemgetter(0))
# Command 14 sorted(fruit.items(), key=operator.itemgetter(1))
# Command 15 sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)
# Command 16 nano user_emails.csv
# Command 17
# Full Name, Email Address
# Blossom Gill, blossom@abc.edu
# Hayes Delgado, nonummy@utnisia.com
# Petra Jones, ac@abc.edu
# Oleg Noel, noel@liberomauris.ca
# Ahmed Miller, ahmed.miller@nequenonquam.co.uk
# Macaulay Douglas, mdouglas@abc.edu
# Aurora Grant, enim.non@abc.edu
# Madison Mcintosh, mcintosh@nisiaenean.net
# Montana Powell, montanap@semmagna.org
# Rogan Robinson, rr.robinson@abc.edu
# Simon Rivera, sri@abc.edu
# Benedict Pacheco, bpacheco@abc.edu
# Maisie Hendrix, mai.hendrix@abc.edu
# Xaviera Gould, xlg@utnisia.net
# Oren Rollins, oren@semmagna.com
# Flavia Santiago, flavia@utnisia.net
# Jackson Owens, jackowens@abc.edu
# Britanni Humphrey, britanni@ut.net
# Kirk Nixon, kirknixon@abc.edu
# Bree Campbell, breee@utnisia.net
# (Note - Save the file by clicking Ctrl-o, Enter key, and Ctrl-x)

# Command 18 sudo chmod +x csv_to_html.py
# Command 19 sudo chmod o+w /var/www/html
# Command 20 ./csv_to_html.py user_emails.csv /var/www/html/file1.html
# Command 21 ls /var/www/html
# Command 22 nano ticky_check.py

# Paste below command in nano editor
# (Replace Student id with the username)

import re
import operator
import csv

error_messages = {}
per_user = {}
#logfile =r"/home/Student id/syslog.log"
logfile = r"syslog.log"
pattern = r"(INFO|ERROR) ([\w' ]+|[\w\[\]#' ]+) (\(\w+\)|\(\w+\.\w+\))$"

with open(logfile, "r") as f:
    for line in f:
        result = re.search(pattern, line)
        if result is None:
            continue
        if result.groups()[0] == "INFO":
            category = result.groups()[0]
            message = result.groups()[1]
            name = str(result.groups()[2])[1:-1]
            if name in per_user:
                user = per_user[name]
                user[category] += 1
            else:
                per_user[name] = {'INFO':1, 'ERROR':0}
        if result.groups()[0] == "ERROR":
            category = result.groups()[0]
            message = result.groups()[1]
            name = str(result.groups()[2])[1:-1]
            error_messages[message] = error_messages.get(message, 0) + 1
            if name in per_user:
                user = per_user[name]
                user[category] += 1
            else:
                per_user[name] = {'INFO':0, 'ERROR':1}
                
sorted_messages = [("Error", "Count")] + sorted(error_messages.items(), key = operator.itemgetter(1), reverse=True)
#sorted_messages = [("Error", "Count")] + sorted(error_messages.items(), key = lambda x: x[1], reverse=True)
sorted_users = [("USERNAME", "INFO", "ERROR")] + sorted(per_user.items())[0:8]
#sorted_users = [("USERNAME", "INFO", "ERROR")] + sorted(per_user.items())

print(sorted_users)

with open("error_message.csv", "w") as error_file:
    for line in sorted_messages:
        error_file.write("{}, {}\n".format(line[0], line[1]))
        
with open("user_statistics.csv", "w") as user_file:
    for line in sorted_users:
        if isinstance(line[1], dict):
            user_file.write("{}, {}, {}\n".format(line[0], line[1].get("INFO"), line[1].get("ERROR")))
        else:
            user_file.write("{}, {}, {}\n".format(line[0], line[1], line[2]))

# Command 23 !/usr/bin/env python3
# Command 24 chmod +x ticky_check.py
# Comamnd 25 ./ticky_check.py
# Command 26 ./csv_to_html.py error_message.csv /var/www/html/file2.html
# Comamnd 27 ./csv_to_html.py user_statistics.csv /var/www/html/file3.html