#!/usr/bin/python3
def func(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    new_arr = set1.union(set2)
    int_arr = set1.intersection(set2)
    f_array = []
    for a in int_arr:
        new_arr.discard(a)
    for b in new_arr:
        f_array.append(b)
    f_array.sort()
    for c in f_array:
        print(c)
    return 0


if __name__ == '__main__':
    m = int(input())
    array1 = list(map(int, input().split()))
    n = int(input())
    array2 = list(map(int, input().split()))
    func(array1, array2)
