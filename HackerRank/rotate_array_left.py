"""
Complete the function rotLeft in the editor below. It should return the resulting array of integers.

rotLeft has the following parameter(s):

An array of integers .
An integer , the number of rotations.
Input Format

The first line contains two space-separated integers  and , the size of  and the number of left rotations you must perform. 
The second line contains  space-separated integers .
"""

def rotLeft(a, d):
    """
    The below algorithm takes advantage of python's powerful slicing functionality to easily 
    re-order our array.

    In Python, index slicing works like so => indices[start:stop:step].

    First, we begin with the index specified at start (k:) and traverse to the next index by our step amount 
    (i.e. if step = 2, then we jump over every other element, if step = 3, we jump over 2 elements at a time). 
    If step is not specified it is defaulted to 1.
    We continue steping from our start point until we come to or exceed our stop point. 
    We do NOT get the stop point, it simply represents the point at which we stop.
    """
    print(a[d:])  # [5]
    print(a[:d])  # [1, 2, 3, 4]
    aR = a[d:] + a[:d]  # [5, 1, 2, 3, 4]
    return aR


print(rotLeft([1, 2, 3, 4, 5], 4))
