# ---------------------- Environment Variables in Linux ---------------------- # 

# Shell:
# A command-line interface used to interact with your operating system.

# Python programs get executed inside a shell command-line environment.

# The variables set in that environment are another source of information
# that we can use in our scripts.

# $PATH - shell uses this environment variable to figure out where to look
# for executeble files, and we call them while specifying a directory.

# Add environment variable:
# execute this command in shell - export VAR_NAME=VALUE
# export FRUIT=Pineapple


import os


print("PyCharm: " + os.environ.get("PyCharm", ""))
print("Chocolatey: " + os.environ.get("ChocolateyPath", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))
