#!/usr/bin/python3
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    val = []
    sums = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        sums = float(sum(scores))
        l = int(len(scores))
        student_marks[name] = float(sums/l)
    query_name = input()
    print("%.2f" % student_marks[query_name])
