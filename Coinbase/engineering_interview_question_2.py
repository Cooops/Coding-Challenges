"""
Asha and Kelly are programming, but Asha practices more than Kelly. Not wanting to fall behind, Kelly resolves to practice more. 
They each solve a number of problems in a day. Asha has already solved more problems than Kelly. What is the minimum number of days
it will take for Kelly to have solved more problems than Asha?

For example, if Asha is 5 problems ahead of Kelly and they solve 3 and 5 problems a day, Asha will be ahead by only 3 after the first day,
1 after the second, and Kelly will pass Asha on day 3.
------------------------------------------------------------------------------------------------------------------------------------------
Complete the function `minNum` in the editor below. The function must return the minimum number of days needed by Kelly to catch up,
or -1 if it's impossible.
"""

# I would like to optimize my code further (specifically when we start iterating over the massive range), but I am not sure how to best to do as of right now.
# Perhaps we should throw the question up on Stack Overflow?

import time
def minNum(A, K, P):
    """
    A:int #of problems asha solves in a day
    K:int #of problems kelly solves in a day
    P:int #of problems asha is ahead to begin with
    """
    # if the delta is 0, kelly is already at parity
    if P == 0:
        return 'she has already reached asha'
    else:
        for i in range(1, 1000000):
            print(f'Asha: {A*i+P} problems')
            print(f'Kelly: {K*i} problems')
            print(f'Diff: {A*i+P-K*i} problems')
            print()
            time.sleep(1)
            # if we are on the second loop and the delta hasn't changed, then the delta will never change.
            if i == 2 and A*i+P-K*i == P:
                return 'she will never reach Asha (diff same) (-1)'
            # otherwise, if the delta is growing, then kelly will never reach asha.
            elif i == 2 and A*i+P-K*i > P:
                return 'she will never reach Asha (diff growing)'
            # otherwise, when kelly passes asha return the number of days it took her
            elif K*i > A*i+P:
                return f'it would take her {i} days'

print(minNum(A=10, K=11, P=2))
