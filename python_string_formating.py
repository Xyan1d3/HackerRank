#!/usr/bin/python3
def print_formatted(N):
    width = len(bin(N)[2:])
    for i in range(1, N + 1):
        print(' '.join(map(lambda x: x.rjust(width), [str(i), oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]])))
