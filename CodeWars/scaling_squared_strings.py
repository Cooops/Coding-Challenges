
# https://www.codewars.com/kata/scaling-squared-strings/python

"""
You are given a string of n lines, each substring being n characters long. For example:

s = "abcd\nefgh\nijkl\nmnop"

We will study the "horizontal" and the "vertical" scaling of this square of strings.

A k-horizontal scaling of a string consists of replicating k times each character of the string (except '\n').

Example: 2-horizontal scaling of s: => "aabbccdd\neeffgghh\niijjkkll\nmmnnoopp"
A v-vertical scaling of a string consists of replicating v times each part of the squared string.

Example: 2-vertical scaling of s: => "abcd\nabcd\nefgh\nefgh\nijkl\nijkl\nmnop\nmnop"
Function scale(strng, k, v) will perform a k-horizontal scaling and a v-vertical scaling.

Example: a = "abcd\nefgh\nijkl\nmnop"
scale(a, 2, 3) --> "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
Printed:

abcd   ----->   aabbccdd
efgh            aabbccdd
ijkl            aabbccdd
mnop            eeffgghh
                eeffgghh
                eeffgghh
                iijjkkll
                iijjkkll
                iijjkkll
                mmnnoopp
                mmnnoopp
                mmnnoopp
#Task:

Write function scale(strng, k, v) k and v will be positive integers. If strng == "" return "".
"""

# MY SOLUTION
def scale(strng, k, n):
    return ''.join([(''.join(letter * k for letter in line) + '\n' ) * n for line in strng.split('\n')]).rstrip()
 
# TOP SOLUTION
def scale_horizontal(strng,k):
    retstrng = strng
    if k > 1:        
        s = [s*k for s in strng]
        retstrng = "".join(s)
    return retstrng
    
def scale(strng, k, n):
    if strng == "": return ""
    lines = strng.split('\n')    
    lines = [scale_horizontal(line,k) for line in lines]
    retlines = []
    for i in range(len(lines)):
        for j in range(n):
            retlines.append(lines[i])
    return "\n".join(retlines)
