#!/usr/bin/python3
def is_leap(year):
    leap = False
    if year == 2100:
        leap == False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
    return leap

