    Instructions
    Output

    This time no story, no theory. The examples below show you how to write function accum:

    Examples:

    accum("abcd")    # "A-Bb-Ccc-Dddd"
    accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    accum("cwAt")    # "C-Ww-Aaa-Tttt"

    The parameter of accum is a string which includes only letters from a..z and A..Z.


def accum(s):
    n = len(s) - 1
    m = len(s)
    b = []
    while n >= 0:
        b.insert(0, s[n:m] * m)
        n -= 1
        m -= 1
    c = ' '.join(map(str, b)).title()
    return c.replace(" ", "-")
    
        
        
