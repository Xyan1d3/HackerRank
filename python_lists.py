#!/usr/bin/python3
if __name__ == '__main__':
    arr = []
    N = int(input())
    for a in range(N):
        p = list(map(str,input().split()))
        if p[0] == "insert":
            arr.insert(int(p[1]),int(p[2]))
        if p[0] == "print":
            print(arr)
        if p[0] == "pop":
            arr.pop()
        if p[0] == "sort":
            arr.sort()
        if p[0] == "reverse":
            arr.reverse()
        if p[0] == "append":
            arr.append(int(p[1]))
        if p[0] == "remove":
            arr.remove(int(p[1])) 

