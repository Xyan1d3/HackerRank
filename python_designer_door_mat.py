#!/usr/bin/python3
(i , j) = map(int,input().split())
s = ".|."
cen_line = int(i/2)
text = "WELCOME"
string = ""
t = 1
a = 0
while a <= cen_line:
    if a < cen_line:
        print("-"*int((j-(t*3))/2)+s*int(t)+"-"*int((j-(t*3))/2))
        t += 2
    elif a == cen_line:
        val = j - 7
        print("-"*int(val/2)+text+"-"*int(val/2))
    a += 1
t -= 2
while a != i:
    if a > cen_line:
        print("-"*int((j-(t*3))/2)+s*int(t)+"-"*int((j-(t*3))/2))
        t -= 2
    a += 1

