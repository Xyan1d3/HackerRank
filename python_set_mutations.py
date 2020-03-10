#!/usr/bin/python3
length=int(input())
s=set(map(int, input().split()))
N=int(input())

for i in range(N):
    (p, q)=input().split()
    s2=set(map(int, input().split()))
    if p=='intersection_update':
        s.intersection_update(s2)
    elif p=='update':
        s.update(s2)
    elif p=='symmetric_difference_update':
        s.symmetric_difference_update(s2)
    elif p=='difference_update':
        s.difference_update(s2)
print (sum(s))

'''n = int(input())
seta = set(list(map(int,input().split())))
cat = int(input())
for a in range(cat):
    (p,q) = input().split()
    val = set(map(int,input().split()))
    if p == "intersection_update":
        seta.intersection_update(val)
    elif p == "update":
        seta.update(val)
    elif p == "symmetric_difference_update":
        seta.symmetric_difference(val)
    elif p == "difference_update":
        seta.difference_update(val)

print(sum(seta))'''

