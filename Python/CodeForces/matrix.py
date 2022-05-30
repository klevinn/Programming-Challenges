# Template by KJHJason

import sys, math

def get_intl(): 
    """Returns a list of integer from stdin"""
    return list(map(int, sys.stdin.readline().strip().split()))
def get_int(): 
    """Returns an integer from stdin"""
    return int(sys.stdin.readline().strip())
def get_strl(): 
    """Returns a list of strings from stdin"""
    return sys.stdin.readline().strip().split()
def get_str(): 
    """Returns a string from stdin"""
    return sys.stdin.readline().strip()
def prt(msg=""):
    """print function using sys.stdout"""
    if (isinstance(msg, list)):
        sys.stdout.write(" ".join(map(str, msg)) + "\n")
    else:
        sys.stdout.write(str(msg) + "\n")

sys.setrecursionlimit(100000000)
MOD = 998244353

def solve():
    line1 = get_intl()
    line2 = get_intl()
    line3 = get_intl()
    line4 = get_intl()
    line5 = get_intl()

    moves = 0

    if sum(line1) != 0:
        index = line1.index(1)
        if index != 2:
            moves += abs(index - 2) + 2 
        else:
            moves += 2

    elif sum(line2) != 0:
        index = line2.index(1)
        if index != 2:
            moves += abs(index - 2) + 1
        else:
            moves += 1

    elif sum(line3) != 0:
        index = line3.index(1)
        if index != 2:
            moves += abs(index - 2)  

    elif sum(line4) != 0:
        index = line4.index(1)
        if index != 2:
            moves += abs(index - 2) + 1
        else:
            moves += 1

    elif sum(line5) != 0:
        index = line5.index(1)
        if index != 2:
            moves += abs(index - 2) + 2 
        else:
            moves += 2

    prt(moves)

def main():
    haveTestCases = 0 # change accordingly
    testCase = 1
    if (haveTestCases):
        testCase = get_int()

    for i in range(testCase):
        solve()

main()