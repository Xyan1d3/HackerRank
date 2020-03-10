#!/usr/bin/python3
if __name__ == '__main__':
    s = input()
    alnu = False
    al = False
    num = False
    low = False
    caps = False
    str_arr = list(s)
    for a in str_arr:
        if a.isalnum():
            alnu = True
        if a.isdigit():
            num = True
        if a.isalpha():
            al = True
        if a.islower():
            low = True
        if a.isupper():
            caps = True
    print(alnu)
    print(al)
    print(num)
    print(low)
    print(caps)



