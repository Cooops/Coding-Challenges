# https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

"""
Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy?
For example, if  and Mark has  to spend, he can buy items  for , or  for  units of currency.
He would choose the first group of  items.

Complete the function maximumToys in the editor below. It should return an integer representing the maximum number of toys Mark can purchase.

maximumToys has the following parameter(s):

prices: an array of integers representing toy prices
k: an integer, Mark's budget
"""
def maximumToys(prices, k):
    # brute force
    # sort the array
    pricesSorted = sorted(prices)
    purchasables = []
    while sum(purchasables) < k:
        purchasables.append(pricesSorted.pop(0))
    print(len(purchasables[:-1]))

print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))  # 4
print(maximumToys([3, 7, 2, 9, 4], 15))  # 3
print(maximumToys([1, 2, 3, 4], 7))  # 3


