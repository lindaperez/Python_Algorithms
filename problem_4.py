#Dutch National Flag Problem
#Given an input array consisting on only 0, 1, and 2, sort the array in a
# single traversal. You're not allowed to use any sorting function that Python provides.

#Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse
# the array twice, that would still be an O(n) solution but it will not count as single traversal.

#Here is some boilerplate code and test cases to start with:


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    n = len(input_list)
    x = 0
    y = x
    z = n-1
    i = 0

    while 0<=x<=y<=z<n:
        if input_list[z] == 2:
            z -= 1
            continue
        if input_list[x] == 0:
            x += 1
            y=x
            continue
        if input_list[y] == 1:
            y += 1
        elif input_list[y]==0:
            aux = input_list[y]
            input_list[y]=input_list[x]
            input_list[x]= aux
        elif input_list[y]==2:
            aux = input_list[z]
            input_list[z] = input_list[y]
            input_list[y] = aux

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)

    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
#expected the array sorted [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
#expected the array sorted
# #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
#expected the array sorted
#[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]


test_function([])
#expected the []

test_function([2])
#expected the [2]

test_function([0, 0, 1, 1, 1, 2, 2, 2]) #expected the array sorted
#[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

test_function([2,2,2,1,1,1]) #expected the array sorted
#[1,1,1,2,2,2]

test_function([ 2,2,2,2,2,2,2,1,1,1,1,0,0,0])
#[0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

test_function([ 0,0,0])
#[ 0,0,0]

test_function([ 0,1,0,1,0, 1, 1, 0,1, 2, 2, 2])
#[0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2]

test_function([ 2,0,1,0,2,1,0,2, 1, 1, 0,1, 2, 2, 2])
#[0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]

test_function([ 2,0,1,0,2,1,0,2, 1, 1, 0,1, 2, 1])
#[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]

test_function([ 2,0,1,0,2,1,0,2, 1, 1, 0,1, 2, 0])
#[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2]

test_function([ 2,2,2,2,2,2,2,1,1,1,1,2,2,2])
#[1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

