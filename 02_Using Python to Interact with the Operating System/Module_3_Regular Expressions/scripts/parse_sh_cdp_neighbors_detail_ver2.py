import re
from pprint import pprint


def parse_cdp(filename):
    regex = (r'Device ID: (?P<device>\S+)'
             r'|IP address: (?P<ip>\S+)'
             r'|Platform: (?P<platform>\S+ \S+),'
             r'|Cisco IOS Software, (?P<ios>.+), RELEASE')

    result = {}

    with open(filename) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                if match.lastgroup == 'device':
                    device = match.group(match.lastgroup)
                    result[device] = {}
                else:
                    result[device][match.lastgroup] = match.group(
                        match.lastgroup)

    return result


pprint(parse_cdp('sh_cdp_neighbors_sw1.txt'))



# Explanations for the second option:

# 1. in the regular expression, all variants of strings are described through the sign | ("or")
# 2. without checking the string, a match is searched
# 3. if a match is found, the lastgroup method is checked
# 4. the lastgroup method returns the name of the last named group in the regular expression for which a match was found
# 5. if a match was found for the device group, the device variable is set to the value that fell into this group
# 6. otherwise, the match "group name" is written to the dictionary: the corresponding value