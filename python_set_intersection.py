#!/usr/bin/python3
a = list(map(int , input().split()))
arr_a = list(map(int , input().split()))
b = list(map(int , input().split()))
arr_b = list(map(int , input().split()))

seta = set(arr_a)
setb = set(arr_b)

uset = seta.intersection(setb)

print(len(uset))

