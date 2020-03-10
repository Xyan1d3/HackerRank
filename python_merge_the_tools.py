#!/usr/bin/python3
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
def merge_the_tools(string, k):
    array = []
    c = 0
    while True:
        array.append(string[c:c+k])
        c += k
        if c == len(string):
            break
    k = k-1
    for a in array:
        char = Remove(list(a))
        str = ""
        print(str.join(char))
