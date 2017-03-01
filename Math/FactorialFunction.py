# Function that calculates factorial of a given number n, using recursion

'''
    The factorial of a positive integer n, denoted n!, is defined as the product of the integers from 1 to n.
    If n=0, then n! is defined as 1 by convention. if n>=1 then n!=n*(n-1)*(n-2).....3*2*1.
    The factorial function is important because it is known to equal the number of ways in which n distinct item can be
    arranged into a sequence, that is, the number of permutations of n items.

    The recursive definition can be formalized as follows:
    n! = 1 if n = 0.
    n! = n*(n-1)! if n>=1.
'''


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
