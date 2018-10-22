# https://www.codewars.com/kata/mumbling

"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""

# MY SOLUTION
def accum(s):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    counter = 0
    finalements = []
    for i in s:
        if i.lower() not in alphabet:
            return 'not in alphabet'
        else:
            counter += 1
            elements = [i for x in range(counter)]
            finalements.append("".join(elements).capitalize())
    return "-".join(finalements)


# TOP SOLUTION
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
