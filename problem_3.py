# ***** Rearrange Array Elements*****#

# ***** PROBLEM DESCRIPTION ********#
# Rearrange Array Elements so as to form two number such that their sum is maximum.
# Return these two numbers. You can assume that all array elements are in the range [0, 9].
# The number of digits in both the numbers cannot differ by more than 1. You're not allowed to
# use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
# for e.g. [1, 2, 3, 4, 5]
# The expected answer would be [531, 42]. Another expected answer can be [542, 31].
# In scenarios such as these when there are more than one possible answers, return any one.
# Here is some boilerplate code and test cases to start with:


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    n = len(input_list)
    if n == 0:
        return [0, 0]
    if n == 1:
        return [input_list[0], 0]

    merge_divide(input_list)
    left  = []
    right = []
    for i in range(n - 1, -1, -1):
        if i % 2 == 0:
            left.append(str(input_list[i]))
        else:
            right.append(str(input_list[i]))

    l = int(''.join(left))
    r = int(''.join(right))
    if ((n - 1) % 2) == 0:
        return [l, r]
    else:
        return [r, l]

def merge_divide(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return arr
    left = arr[:n // 2]
    right = arr[n // 2:]
    merge_divide(left)
    merge_divide(right)
    ans = conquer_merge(arr, left, right)
    return ans

def conquer_merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr[k] = right[j]
            j += 1
        else:
            arr[k] = left[i]
            i += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]

    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_case = [[4, 6, 2, 5, 9, 8,99], [99864,952]] #expected sum(99864,952)
test_function(test_case)
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]] #expected sum(964,852)
test_function(test_case)
test_case = [[1, 2, 3, 4, 5], [542, 31]] #expected sum(542,31)
test_function(test_case)
test_case = [[4, 2, 3], [43, 2]] #expected sum(43,2)
test_function(test_case)
test_case = [[1,3], [3, 1]] #expected sum(3,1)
test_function(test_case)
test_case = [[1], [1, 0]] #expected sum(1,0)
test_function(test_case)
test_case = [[], [0, 0]] #expected sum(0,0)
test_function(test_case)
