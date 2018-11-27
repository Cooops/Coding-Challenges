# https://www.hackerrank.com/challenges/ctci-ransom-note/forum?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# Using python collections:

from collections import Counter

def checkMagazine(magazine, note):
    """
    The result of counters' operator substraction is a counter that shows how many more values magazine is missing to match
    those present in rasom. When an empty dict is returned, every element in rasom is present enough times in magazine.

    Example:

    x = ['two', 'times', 'three', 'is', 'not', 'four']
    y = ['two', 'times', 'two', 'is', 'four']
    print(checkMagazine(x, y))
    >>> False
    """
    # dict version
    print(Counter(note))
    print(Counter(magazine))  # Counter({'two': 1, 'times': 1, 'three': 1, 'is': 1, 'not': 1, 'four': 1})
    print(Counter(note) - Counter(magazine))  # Counter({'two': 1})
    return 'No' if (Counter(note) - Counter(magazine)) == {} else 'Yes'  # False
    # or...
    # return not (Counter(note) - Counter(magazine))  # False

    # brute force version (works for 2/3 test cases)
    # tally = 0
    # while tally < len(note):
    #     for word in note:
    #         if word in magazine:
    #             tally += 1
    # return True if tally == len(note) else False


# x = ['give', 'me', 'one', 'grand', 'today', 'night']
# y = ['give', 'me', 'one', 'grand', 'today']
x = ['two', 'times', 'three', 'is', 'not', 'four']
y = ['two', 'times', 'two', 'is', 'four']
print(checkMagazine(x, y))
