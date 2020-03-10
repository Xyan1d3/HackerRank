#!/usr/bin/python3
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxa = -9999999999999999999999999999999999
    maxa2 = -9999999999999999999999999999999999
    for a in arr:
        if a > maxa:
            maxa = a
    for b in arr:
        if b > maxa2 and  b < maxa:
            maxa2 = b
    print(maxa2)

