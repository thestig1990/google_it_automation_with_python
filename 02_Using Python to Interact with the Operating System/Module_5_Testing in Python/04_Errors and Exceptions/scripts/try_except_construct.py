#!/usr/bin/env python3

import sys

def character_frequency(filename):
    """Counts the frequency of each character in the given file."""
    # First try to open the file
    try:
        f = open(filename)
    except OSError:
        return None
    
    # Now process the file
    character = {}
    for line in f:
        for char in line:
            character[char] = character.get(char, 0) + 1
    f.close()
    return character


filename = sys.argv[0]
print(character_frequency(filename))