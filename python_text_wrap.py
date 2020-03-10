#!/usr/bin/python3

def wrap(string, max_width):
    l = len(string)
    a = 0
    for d in range(l):
        if (a+max_width) <= l:
            print(string[a:a+max_width])
            a += max_width
        elif (a+max_width) > l:
            print(string[a:l])
            break
    return ""


