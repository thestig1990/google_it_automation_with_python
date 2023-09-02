# -*- coding: utf-8 -*-
import re


#'00:09:BB:3D:D6:58   10.1.10.2        86250       dhcp-snooping   10    FastEthernet0/1'

regex = r'(?P<mac>\S+) +(?P<ip>\S+) +\d+ + \S+ +(?P<vlan>\d+) +(?P<port>\S+)'
result = []

with open('dhcp_snooping.txt',) as data:
    for line in data:
        match = re.search(regex, line)
        if match:
            result.append(match.groupdict())


print(f'There are {len(result)} devices connected to the switch')

for num, comp in enumerate(result, 1):
    print(f'Device parametrs №{num}')
    for key in comp:
        print(f'{key:10}: {comp[key]:10}')