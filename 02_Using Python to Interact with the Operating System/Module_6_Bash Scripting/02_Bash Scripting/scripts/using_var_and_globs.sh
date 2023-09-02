#!/usr/bin/bash

line="--------------------------------------------------------------"
echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHOAMI"; whoami; echo $line

echo "Finishing at: $(date)"