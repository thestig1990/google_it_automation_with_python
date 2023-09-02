#!/usr/bin/env python3

import sys
import re

print(f"sys.argv ---> {sys.argv}")


logfile= sys.argv[1]
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)"
        result = re.search(pattern, line)
        #print(result.group())
        print(f"User: {result[1]}")
        
        
        