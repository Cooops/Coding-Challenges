# https://www.codewars.com/trainer/python
"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""

# MY SOLUTION
def XO(s):
    return s.lower().count('o') == s.lower().count('x')

# TOP SOLUTION
def XO(s):
    s = s.lower()
    return s.count('x') == s.count('o')
