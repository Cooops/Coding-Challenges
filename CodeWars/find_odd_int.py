# http://www.codewars.com/kata/find-the-odd-int/python

# MY SOLUTION
def find_it(n):
    """ (array) -> int

    Takes in an array of integers and returns the int that appears an odd number of times.
    There will always be _only one_ integer that appears an odd number of times.
    
    We use .pop to pop the last value out of the set. We can also use `next(iter(set(list)))` to extract the value.
    """
    return set([i for i in n if n.count(i) % 2]).pop()
    
# TOP SOLUTION
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
