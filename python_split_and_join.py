#!/usr/bin/python3
def swap_case(s):
    str_arr = []
    f_str = ""
    for a in range(len(s)):
        str_arr.append(s[a])
    for b in str_arr:
        if b.isupper():
            f_str += b.lower()
        elif b.islower():
            f_str += b.upper()
        else:
            f_str += b
    return f_str


