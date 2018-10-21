from itertools import combinations, permutations
import math

def square_sums_row(n):
    array = list(range(1, n+1))
    return array

values = square_sums_row(15)
firstElement = values[1:]
lastElement = values[:-1]
# allCombinations = cominbations(values, 2)
allCombinations = combinations(values, 2)
memo = {}
summed = []
for i in allCombinations:
    # print(sum(i))
    summed.append(sum(i)**.5%1)
    memo[i] = sum(i)**.5%1

# print(summed.count(0.0), math.ceil(len(values)/2))
# print(i for i in list(memo))
# print(memo)
try:
    assert summed.count(0.0) >= math.ceil(len(values)/2)  # round up and assert that the maximum number of perfect squares exceeds the length of the initial input value divided by 2.
    print('True')
    # print(summed)
    # print(memo)
    perfectSquares = list((i, memo[i]) for i in memo if memo[i] == 0.0)
    for i in perfectSquares:
        print(i)
        # print(f'{i[0][0], i[0][1]} ', end="")

        # print(i[0][0], i[0][1])

        # if i[0][0]+i[0][1]**.5%1 != 0:
        #     print('not a perfect square')
        # else:
        #     print('perfect square')
    # print(perfectSquares)
except AssertionError:
    print('False')  # return False if the length does not match, as that means that we could not create the maximum number of squares.
    print(list((i, memo[i]) for i in memo if memo[i] == 0.0))
    # print(summed)


# for i in zip(firstElement, lastElement):
#     print(i)
#     # we need everything below to spit out 0's, otherwise there is _not_ a possible sequence to generate 100% perfect squares.
#     print(sum(i)**.5%1)  # print(i**.5%1)  # if i to the power of .5 divided by 1 does not equal 0, then the value is _not_ a perfect square.


