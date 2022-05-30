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
    nums = get_intl()
    if nums[0] > nums[1]:
        prt("0 0")
    else:
        divisor = nums[1] / nums[0]
        if divisor > 10**9:
                while True:
                    i = 2
                    new = divisor ** (1/i)
                    if new.is_integer():
                        prt(i,int(new))
                        break
        elif divisor.is_integer() != True:
            prt("0 0")
        else:
            prt("1 %d" %(divisor))

def main():
    haveTestCases = 1 # change accordingly
    testCase = 1
    if (haveTestCases):
        testCase = get_int()

    for i in range(testCase):
        solve()

main()