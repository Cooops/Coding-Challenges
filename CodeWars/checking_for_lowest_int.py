# N is between 1 and 100,000
# A is between -1,000,000 and 1,000,000

# Find smallest positive int that does not occur in A

def solution(A):
    """O(N) or O(N * log(N))"""
    A = set(A)  # cast to a set to remove all duplicates
    i = 1  # set incrementor == 1 (greater than 0)
    while i in A:  # if the incrementor is in our array
        i += 1  # increment it and repeat. this continues until we find the lowest missing number
    return i

A1 = [1,2,3,4,1,2]
A2 = [-1, -3]
resA1 = solution(A1)
resA2 = solution(A2)

assert resA1 == 5
assert resA2 == 1

print(resA1)
print(resA2)
