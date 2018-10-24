# http://www.codewars.com/kata/vowel-count/train/python

"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.

print(getCount("abracadabra"))
print(getCount("brdbr"))
print(getCount("aeiouaeiou"))
"""

# MY SOLUTION
def getCount(inputStr):
    vowels = ["a", "e", "i", "o", "u"]
    x = [inputStr.count(vowel) for vowel in vowels if vowel in list(inputStr)]
    return sum(x) if len(x) >= 1 else 0

# TOP SOLUTION
def getCount(inputStr):
    return sum(c in 'aeiou' for c in s)
    
