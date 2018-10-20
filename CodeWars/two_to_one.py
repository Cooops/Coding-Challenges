"""
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,
each taken only once - coming from s1 or s2. 

#Examples: 
``` 
a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b) -> "abcdefklmopqwxy"
a = "abcdefghijklmnopqrstuvwxyz" longest(a, a) -> "abcdefghijklmnopqrstuvwxyz" 
```
"""
from collections import OrderedDict

# MY SOLUTION
def longest(s1, s2):
    """ (list) -> list

    Reads in any number of lists and returns a _sorted_ string, containing distinct letters. 
    If order didn't matter, we could use a set, but since it does we need to use an ordered dictionary.
    """
    mergedList = s1 + s2
    mergedList = list(mergedList)
    mergedList.sort()
    return ''.join(list(OrderedDict.fromkeys(mergedList)))

print(longest("aretheyhere", "yestheyarehere"))

# TOP SOLUTION
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


