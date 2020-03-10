#!/usr/bin/python3
a = list(map(int,input().split()))
arr_a = set(list(map(int,input().split())))
b = list(map(int,input().split()))
arr_b = set(list(map(int,input().split())))

uset = arr_a.symmetric_difference(arr_b)
print(len(uset))
