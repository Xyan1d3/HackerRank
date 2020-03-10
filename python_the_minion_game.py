#!/usr/bin/python3
def minion_game(string):
    stuart = 0
    kevin = 0
    vow = ['A','E','I','O','U']
    for a in range(len(string)):
        if string[a] in vow:
            kevin +=  len(string) - a
        else :
            stuart += len(string) - a
    if kevin > stuart:
        print ("Kevin "+str(kevin))
    elif stuart > kevin:
        print ("Stuart "+str(stuart))
    else:
        print ("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
