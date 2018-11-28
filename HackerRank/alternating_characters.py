# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

"""
Complete the alternatingCharacters function in the editor below. It must return an integer representing the minimum number of deletions to make the alternating string.

alternatingCharacters has the following parameter(s):

s: a string
"""

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    # # for each in s:
    # #     # print(each)
        
    # #     # brute force
    # #     print(each)
    # a = 'A'
    # b = 'B'
    # # newWord = [s[0]]
    # newWord = []
    # deletions = 0
    # # brute force
    # for letter in s:
    #     newWord.append(letter)
    #     if letter == newWord[-1]:
    #         deletions += 1
    #         # pass
    # print(deletions)

    # sort it
    # make it into a set
    # subtract the diff in len?
    # for i in s:
    #     lenS = len(i)
    #     setS = len(set(i))
    #     # print(lenS)
    #     # print(setS)
    #     if lenS == (lenS - setS):
    #         print('0')
    #     print(lenS - setS)
    for s in s:
        print(sum(s[i]==s[i+1]for i in range(len(s)-1)))

# alternatingCharacters('AAAA')  # 3
alternatingCharacters(['AAAA', 'BBBBB', 'ABABABAB', 'BABABA', 'AAABBB'])  # 3, 4, 0, 0, 4
