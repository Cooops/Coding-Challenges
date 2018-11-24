def overlapping_time(arr):
    # we use a key that extracts the value by which to sort; in this case the first element in the list,
    # as we want to sort based on the starting meeting time in ascending order, 
    # as it allows us to easily iterate over the meeting array and know our new meeting times won't overlap with previous meetings
    arrS = sorted(arr, key=lambda i: i[0])
    # we extract the first meeting in the array, along with the first meeting's end time, 
    # which we will compare future start meeting times against
    firstMeeting = arrS[0]
    firstMeetingEnd = firstMeeting[1]
    # bool check we will set to True if we find overlapping meetings
    overlap = False
    for meeting in arrS[1:]:  # for every meeting after the first
        if meeting[0] <= firstMeetingEnd:  # if the new meeting time is equal to or less than the first, we have found an overlap
            overlap = True, 'Overlap'
            return overlap
        firstMeetingEnd = meeting[1]  # otherwise assing our new meeting time as the current meeting's end time, and repeat the process
    return overlap, 'No overlap'
    
arr1 = [[1, 3], [5, 7], [2, 4], [6, 8]]  # True, [1, 3] and [2, 4] overlap
arr2 = [[1, 3], [7, 9], [4, 6], [10, 13]]  # False
print(overlapping_time(arr1))
print(overlapping_time(arr2))
