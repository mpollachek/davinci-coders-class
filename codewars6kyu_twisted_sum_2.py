"""
Find the sum of the digits of all the numbers from 1 to N (both ends included).

For N = 10 the sum is 1+2+3+4+5+6+7+8+9+(1+0) = 46

For N = 11 the sum is 1+2+3+4+5+6+7+8+9+(1+0)+(1+1) = 48

For N = 12 the sum is 1+2+3+4+5+6+7+8+9+(1+0)+(1+1) +(1+2)= 51

"""

def compute_sum(n):
    a = []                                   #empty list to put values in every loop
    extra = 0                                #every time n goes up 10 we need to increase this by 1
    while n > 0:
        if n <= 9 and n > 0:
            b = sum(range(0, n+1)) + (extra * n)
        elif n > 9:
            b = sum(range(0, 10)) + (extra * 10)
            extra += 1
        a.append(b)
        n -= 10
    print sum(a) + extra

