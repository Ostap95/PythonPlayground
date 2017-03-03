'''
    When the sequence is unsorted, the standard approach to search for a target value is to use a loop to examine
    every element in the data set until the element is found. This is known as the sequential search algorithm.
    This algorithm runs in O(n) time.

    When the sequence is sorted we don't have to inspect every element of the data set. There is a better algorithm.
    For any index j, we know that all the values stored at indices 0,...,j-1 are less than or equal to the value at
    index j, and all the values stored at indices j+1,..., n-1 are greater than or equal to that at index j.
    The algorithm maintains 2 parameters, 'low' and 'high' such that all the candidate entries have index at least low
    and at most high. Initially, low = 0 and high = n - 1. We then compare the target value to the median candidate.

    3 cases:
        If the target equal data[mid], then we have found the element that we are looking for, and the search terminates
        successfully.
        If target < data[mid], then we recur on the first half of the sequence, that is, on the interval of indices from
        low to mid - 1.
        If target > data[mid], then we recur on the second half of the sequence, that is, on the interval of indices from
        mid + 1 to high.

    An unsuccessful search occurs if low > high, as the interval [low, high] is empty.

    Whereas sequential search runs in O(n) time, the more efficient binary search runs in O(log*n) time.
'''


def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

