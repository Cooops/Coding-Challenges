# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

# Complete the countSwaps function below.
"""
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
"""

swaps = 0

def countSwaps(a):
    global swaps
    firstNum = min(a)
    lastNum = max(a)  # the max number will always be what we want to iterate up to

    for i in range(len(a)):
        try:
            if a[i] > a[i+1]:  # if the elements are descending
                swaps += 1
                a[i], a[i+1] = a[i+1], a[i]  # this is how we re-arrange elements in python (more: https://stackoverflow.com/questions/14836228/is-there-a-standardized-method-to-swap-two-variables-in-python)
                countSwaps(a)  # recursively call function until we meet our desired result (no more descending numbers)
        except:
            # end of list
            return f"Array is sorted in {swaps} swaps.\nFirst Element: {firstNum}\nLast Element: {lastNum}"
            break



# print(countSwaps([1, 2, 3]))  # no swaps
# print(countSwaps([3, 2, 1]))  # 3 swaps
print(countSwaps([4, 2, 3, 1]))  # 5 swaps
