# ***** Search in a Rotated Sorted Array*****#

# ***** PROBLEM DESCRIPTION ********#
# You are given a sorted array which is rotated at some random pivot point.
# Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# You can assume there are no duplicates in the array and your algorithm's
# runtime complexity must be in the order of O(log n).
# Example:
# Input: arr = [4,5,6,7,0,1,2], target = 0, Output: 4
# Here is some boilerplate code and test cases to start with:
import random
def rotated_array_search(input_list, number) -> int:
    """
        Find the index by searching in a rotated sorted array

        Args:
           input_list(array), number(int): Input array to search and the target
        Returns:
           int: Index or -1
        """
    arr = input_list
    target = number
    n = len(arr)
    if n == 0: return -1
    if n == 1: return 0 if arr[0] == target else -1
    pivot = find_pivot(arr, 0, n - 1)
    if pivot == 0:
        return binary_search(arr, target, 0, n - 1)
    if target < arr[0]:
        return binary_search(arr, target, pivot, n - 1)

    return binary_search(arr, target, 0, pivot)


def binary_search(arr, target, left, right) -> int:
    """
       Find the index by searching in a sorted array

       Args:
          arr(array), target(int): Input array to search and the target
          left, right: Indexes min and max
       Returns:
          int: Index or -1
       """

    while (0 <= left <= right < len(arr)):
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        elif arr[middle] > target:
            right = middle - 1
    return -1


def find_pivot(arr, left: int, right: int)->int:
    """
       Find the pivot location min,max

       Args:
          arr(array): Input array to search and the pivot
          left, right: Indexes min and max
       Returns:
          int: Pivot or -1
    """

    if arr[left] < arr[right]:
        return 0

    while (left <= right):
        middle = (left + right) // 2
        if arr[middle] > arr[middle + 1]:
            return middle + 1
        else:
            if arr[middle] < arr[left]:
                right = middle - 1
            else:
                left = middle + 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


#***** Test Cases *****#

assert (find_pivot([1, 5, 6, 8, 9, 0], 0, 5) == 5)  # min number from array position 5
assert (find_pivot([2, 5, 6, 0, 1], 0, 4) == 3) # min number from array position 3
assert (find_pivot([1, 5, 6, 8, 9, 11], 0, 5) == 0) # min number from array position 0


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]

    if linear_search(input_list, number) == rotated_array_search(input_list, number):

        print("Pass")
    else:
        print("Fail")

test_function([[], 4])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[4, 5, 6, 7, 0, 1, 2], 4])
test_function([[6, 7, 8, 9, 10, 12, 22, 43, 54,67,91,-34,3,2], -34])
test_function([[6, 7, 8, 9, 10, 12, 22, 43, 54,67,91,-1,1,3], -88])
l = [i for i in range(-900, 100000)]  # a list containing 0 - 9
test_function([l, -956])
m= [i for i in range(-9090, 10000099)]  # a list containing 0 - 9
test_function([m, 10000098])

