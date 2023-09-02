import re


log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Perfoming package upgrade"
regex = r"\[(\d+)\]"
match = re.search(regex, log)
print(match.groups())
print(match.group())
print(match[1])

print()

match = re.search(regex, "A completely different string that also has numbers [34567]")
print(match[1])


print()


# defining fuction "extract_pid"
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    match = re.search(regex, log_line)
    if match is None:
        return "Nothing match"
    return match[1]


print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]"))


print()


# Add to the regular expression used in the extract_pid function, 
# to return the uppercase message in parenthesis, after the process id.
import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
