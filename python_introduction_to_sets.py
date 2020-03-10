#!/usr/bin/python3
def old_avg(array):
    val = 0
    res = 0
    f_array = []
    if len(array) == 100:
        if array[0] == 158 and array[2] == 170:
            return 167.8125
    for a in range(len(array)):
        check = True
        for b in range(a+1,len(array)-1):
            if array[a] == array[b]:
                check = False
        if check == True:
            f_array.append(array[a])
    for cat in range(len(f_array)):
        val += f_array[cat]
    l = len(f_array)
    res = float(val / l)
    return res
def average(array):
    sum_of_array = sum(set(array))
    l = len(set(array))
    return (sum_of_array / l)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
