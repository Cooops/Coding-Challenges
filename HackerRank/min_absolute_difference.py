# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

"""
Consider an array of integers, . We define the absolute difference between two elements,  and  (where ), to be the absolute value of .

Given an array of integers, find and print the minimum absolute difference between any two elements in the array. For example, given the array  we can create  pairs of numbers:  and . The absolute differences for these pairs are ,  and . The minimum absolute difference is .

Function Description

Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents the minimum absolute difference between any pair of elements.

minimumAbsoluteDifference has the following parameter(s):

n: an integer that represents the length of arr
arr: an array of integers
"""

from itertools import combinations

def minimumAbsoluteDifference(arr):
    coms = list(combinations(arr, 2))
    # normally -7, etc. but we convert it to the absolute which is simply 7 (converts neg -> pos in this instance)
    # https://docs.python.org/3/library/functions.html#abs
    hits = [abs(i[0]-i[1]) for i in coms]
    return min(hits) 

minimumAbsoluteDifference([3, -7, 0])  # 3
