#!/usr/bin/env python3
import subprocess
src = "/data/prod/"
dest = "/data/prod_backup/"
subprocess.call(["rsync", "-arq", src, dest])
