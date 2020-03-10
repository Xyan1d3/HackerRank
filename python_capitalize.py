#!/usr/bin/python3
import math
import os
import random
import re
import sys

def solve(s):
    caps = False
    f_str = ""
    for a in range(len(s)):
        if caps == False and a != 0:
            f_str += s[a]
        if caps == True or a == 0:
            f_str += s[a].upper()
            caps = False
        if s[a].isspace():
            caps = True
    return f_str
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

