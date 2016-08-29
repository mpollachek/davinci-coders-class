Take a number: 56789. Rotate left, you get 67895.

Keep the first digit in place and rotate left the other digits: 68957.

Keep the first two digits in place and rotate the other ones: 68579.

Keep the first three digits and rotate left the rest: 68597. Now it is over since keeping the first four it remains only one digit which rotated is itself.

You have the following sequence of numbers:

56789 -> 67895 -> 68957 -> 68579 -> 68597

and you must return the greatest: 68957.

Calling this function max_rot (or maxRot or ... depending on the language)

max_rot(56789) should return 68957



def max_rot(n):
    a = list(str(n))                  #turn number into a list of digits
    b = [n]                           #create list to put all final numbers in
    index = 0                         #index is location of number you are moving
    end = len(a) - 1                  #last index in list is length minus 1
    while index <= end - 1:           
        a.insert(end, a.pop(index))   #pop out indexed number and insert at end
        y = ''.join(map(str, a))      #convert list (a) to string and join as 1 number
        b.insert(-1, y)               #add number to list (b)
        index +=1                     #add 1 to index
    return max(b)                     #return highest number in list (b)

