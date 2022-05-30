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
def prtY():
    """print "YES" using sys.stdout"""
    sys.stdout.write("YES\n")
def prtN():
    """print "NO" using sys.stdout"""
    sys.stdout.write("NO\n")
def prtYN(cond):
    """print "YES" or "NO" using sys.stdout
    
    args: 
    - cond (bool): if true, print "YES", else print "NO"
    """
    if (cond):
        prtY()
    else:
        prtN()

sys.setrecursionlimit(100000000)
MOD = 998244353

def solve():
    init = get_str()
    repl = get_str()
    if len(repl) == 1 and repl == "a":
        prt(1)
    elif len(repl) == 1 and len(init) == 1:
        prt(2)
    elif len(repl) > 1 and "a" in repl:
        prt(-1)
    else:
        prt((len(init)*(len(init)+1) // 2))

def main():
    haveTestCases = 1 # change accordingly
    testCase = 1
    if (haveTestCases):
        testCase = get_int()

    for i in range(testCase):
        solve()

main()