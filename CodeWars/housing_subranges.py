"""
https://github.com/tinytheyfon8/amne-coding-challenge

Challenge #1

As Amne expands, we will want to understand large-scale patterns in home values.

As we look at patterns across windows of certain sizes, we will need to efficiently track trends such as increasing and decreasing subranges.

For this problem, you are given N days of average home sale price data, and a fixed window size K . For each window of K days, from left to right, find the number of increasing subranges within the window minus the number of decreasing subranges within the window.

A window of days is defined as a contiguous range of days. Thus, there are exactly N-K+1 windows where this metric needs to be computed. An increasing subrange is defined as a contiguous range of indices [a,b], a < b , where each element is larger than the previous element. A decreasing subrange is similarly defined, except each element is smaller than the next.

Constraints

1 ≤ N ≤ 200,000 days 1 ≤ K ≤ N days Input Format

Your solution should accept an input file (input.txt) with the following contents:

Line 1: Two integers, N and K.  Line 2: N positive integers of average home sale price, each less than 1,000,000.

Output Format

Your solution should output one integer for each window’s result, with each integer on a separate line, to an output file or to the console.

Sample Input

5 3 188930 194123 201345 154243 154243

Sample Output

3 0 -1

Explanation

For the first window of [188930, 194123, 201345], there are 3 increasing subranges ([188930, 194123, 201345], [188930, 194123], and [194123, 201345]) and 0 decreasing, so the answer is 3. For the second window of [194123, 201345, 154243], there is 1 increasing subrange and 1 decreasing, so the answer is 0. For the third window of [201345, 154243, 154243], there is 1 decreasing subrange and 0 increasing, so the answer is -1.

Performance

Your solution should run in less than 30 seconds and use less than 50MB of memory with a valid input of any size (within the given constraints).
"""

import time

def dataset_trend(dataset, days, windows):
    # store hits in dict to allow us to easily index each window
    hits = {}
    counter = 0
    for subrange in dataset:
        counter += 1
        # if the first subset of numbers increases...
        if subrange[0] < subrange[1]:
            hits[counter] = 1
            if subrange[1] < subrange[2]:  # if we hit a series of increases, increment by 2
                hits[counter] += 2
            elif subrange[1] > subrange[2]:  # otherwise, we reduce it by one if it is a negative subrange
                hits[counter] -= 1
            else:
                hits[counter] += 0
        # if the first subset of numbers decreases...
        elif subrange[0] > subrange[1]:
            hits[counter] = -1
            if subrange[1] < subrange[2]:
                hits[counter] -= 2
            elif subrange[1] > subrange[2]:
                hits[counter] += 1
            else:
                hits[counter] += 0
                
    print(f"The dataset consists of {days} days worth of data and there are {windows} windows we need to account for.")
    print(f"The dataset is as follows: {dataset}.")
    for key in hits:
        print(f"First subrange trend: {hits[key]}")

def build_dataset():
    file = open('input.txt', 'r')
    data = file.readlines()

    days = data[0][0]
    windows = data[0][2]
    dataset = data[1]
    dataset = dataset.split()

    # if we needed to automate this/account for more than just three windows, 
    # we could set i = to windows and slice by x ranges across the dataset while incrementing each start:end slice by 1.

    # split datasets into their respective windows
    firstDataset = dataset[0:3]
    secondDataset = dataset[1:4]
    thirdDataset = dataset[2:5]
    dataset = [firstDataset, secondDataset, thirdDataset]

    dataset_trend(dataset, days, windows)

build_dataset()
