# http://www.codewars.com/kata/shortest-word/train/python

"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

# MY SOLUTION
def find_short(s):
    # your code here
    return min([len(i) for i in s.split()])

# TOP SOLUTION
Same thing :)
