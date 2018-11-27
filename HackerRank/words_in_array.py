# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen

from collections import Counter

def twoStrings(s1, s2):
    # baseLen = len(Counter(s1)) + len(Counter(s2))
    # return 'YES' if len(Counter(s1) - Counter(s2)) < baseLen else 'NO'
    return 'YES' if any(substring in s1 for substring in s2) else 'NO'

print(twoStrings('hello', 'world'))
