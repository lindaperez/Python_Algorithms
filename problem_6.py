# ***** Max and Min in a Unsorted Array *****#

# ***** PROBLEM DESCRIPTION ********#/
#In this problem, we will look for smallest and
# largest integer from a list of unsorted integers.
# The code should run in O(n) time. Do not use Python's
# inbuilt functions to find min and max.


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    n = len(ints)
    if n == 0: return (0,0)
    if n == 1: return (ints[0],ints[0])
    min_ = ints[0]
    max_ = ints[0]
    for i in range(n):
        if ints[i]< min_:
            min_ = ints[i]
        if ints[i]>max_:
            max_ = ints[i]
    return (min_,max_)
    pass

## Example Test Case of Ten Integers
import random

l = [i for i in range(-9, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((-9, 9) == get_min_max(l)) else "Fail") # should return -9,9 from an unsorted array
random.shuffle(l)
print ("Pass" if ((-9, 9) == get_min_max(l)) else "Fail") # should return -9,9 from an unsorted array
random.shuffle(l)
print ("Pass" if ((-9, 9) == get_min_max(l)) else "Fail") # should return -9,9 from an unsorted array

print ("Pass" if ((0, 0) == get_min_max([])) else "Fail") # should return 0,0 because no elements