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
    inp = get_int()
    if inp % 2 == 0:
        prt(int(inp / 2))
    else:
        prt(int((inp - 1) / 2 - inp))

def main():
    haveTestCases = 0 # change accordingly
    testCase = 1
    if (haveTestCases):
        testCase = get_int()

    for i in range(testCase):
        solve()

main()