#!/bin/bash

list_of_files=/var/log/*log

for logfile in $list_of_files; do
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done