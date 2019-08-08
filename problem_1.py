#***** Finding the Square Root of an Integer *****#

#***** PROBLEM DESCRIPTION ********#
# Find the square root of the integer without using any Python library.
# You have to find the floor value of the square root.
# For example if the given number is 16, then the answer would be 4.
# If the given number is 27, the answer would be 5 because sqrt(5) = 5.196
# whose floor value is 5.
# The expected time complexity is O(log(n))

import math
def sqrt(number: int)-> int:
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    try:
        if number<0:
            raise ValueError
        if 0<=number<=4:
            for i in range(number,0,-1):
                if i * i <= number:
                    return i
            return 0
        else:
            arr = list(range(0, number // 2))
            return binary_search(arr, number)
    except ValueError:
        print("ValueError:Negative number does not have a square root")
        return -1

def binary_search(arr, target) -> int:
    """
        Calculate the index of a number "target"

        Args:
           arr(int): Array to find the target
           target(int): Number to find the index
        Returns:
           int: Index position of array
        """

    if len(arr) == 0: return -1
    left = 0
    right = len(arr) - 1
    middle = (left + right) // 2
    while 0 <= left <= right < len(arr):
        if arr[middle]<0:
            raise ValueError
        if (arr[middle] * arr[middle]) == target:
            return middle
        elif (arr[middle] * arr[middle]) < target:
            left = middle + 1
        elif (arr[middle] * arr[middle]) > target:
            right = middle - 1
        middle = (left + right) // 2
    return middle


##Test Cases##

assert(binary_search([],0) == -1)           #especting 0 due list is empty and not found the element
assert(binary_search([1,2,3,4,5],1) == 0)   #especting 0 due to 1*1<=1 is in the position 0
assert(binary_search([1,2,3,4,5],2) == 0)   #especting 0 due to 1*1<=2 is in the position 0
assert(binary_search([1,2,3,4,5],3) == 0)   #especting 0 due to 1*1<=3 is in the position 0
assert(binary_search([1,2,3,4,5],4) == 1)   #especting 0 due to 2*2<=4 is in the position 1
assert(binary_search([1,2,3,4,5],5) == 1)   #especting 0 due to 2*2<=5 is in the position 1


assert (sqrt(0) == math.floor(math.sqrt(0))) #especting 1 sqrt(1)
assert (sqrt(1) == math.floor(math.sqrt(1))) #especting 1 sqrt(1)
assert (sqrt(2) == math.floor(math.sqrt(1))) #especting 1 floor of sqrt(2)
assert (sqrt(4) == math.floor(math.sqrt(4))) #especting 2 floor of sqrt(4)

print ("Pass" if  (math.floor(math.sqrt(88)) == sqrt(88)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")

print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  ( math.floor(math.sqrt(213))== sqrt(213)) else "Fail")
print ("Pass" if  (math.floor(math.sqrt(5432)) == sqrt(5432)) else "Fail")
print ("Pass" if  (math.floor(math.sqrt(2048)) == sqrt(2048)) else "Fail")
print ("Pass" if  (math.floor(math.sqrt(2047)) == sqrt(2047)) else "Fail")
print ("Pass" if  (math.floor(math.sqrt(82041)) == sqrt(82041)) else "Fail")
print ("Pass" if  (math.floor(math.sqrt(204732)) == sqrt(204732)) else "Fail")
print ("Pass" if  (math.floor(math.sqrt(56204730)) == sqrt(56204730)) else "Fail")
print ("Pass" if  (math.floor(math.sqrt(10000000)) == sqrt(10000000)) else "Fail")
print ("Pass" if  (-1 == sqrt(-64)) else "Fail")




