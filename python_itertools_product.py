#!/usr/bin/python3
from itertools import product as pro

c = 0
f_str = ""
arr_a = list(map(int,input().split()))
arr_b = list(map(int,input().split()))
f = list(pro(arr_a,arr_b))

for a in f:
    if c == 0:
        f_str = f_str + "" + str(a)
        c += 1
    else:
        f_str = f_str + " " + str(a)
print(f_str)

