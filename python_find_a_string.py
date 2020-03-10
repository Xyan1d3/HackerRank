#!/usr/bin/python3
def count_substring(s1, s2):

    cnt = 0
    for i in range(len(s1)):
        if s1[i:].startswith(s2):
            cnt += 1
    return cnt


