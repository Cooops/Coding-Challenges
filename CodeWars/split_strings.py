# https://www.codewars.com/kata/split-strings/train/python

"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""

# MY solution
def solution(s):
    x = [s[i:i+2] for i in range(0, len(s), 2)]  # we use range steps to force-slice every 2 elements.
    if len(s)%2!=0:
        x[-1] += '_'
    return x

# TOP SOLUTION
import re

def solution(s):
    return re.findall(".{2}", s + "_")
    
