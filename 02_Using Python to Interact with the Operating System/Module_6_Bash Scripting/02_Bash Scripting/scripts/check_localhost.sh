#!/bin/bash

ip="127.0.0.1"
path="/etc/hosts"
if grep $ip $path; then
    echo "Everything ok"
else
    echo "ERROR! $ip is not in $path"
fi