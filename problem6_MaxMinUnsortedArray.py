"""
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
    	return

    if len(ints) == 1:
    	return (ints[0], ints[0])

    curr_max = ints[0]
    curr_min = ints[0]

    for ele in ints[1:]:
    	if ele < curr_min:
    		curr_min = ele
    	if ele > curr_max:
    		curr_max = ele
    print(curr_max, curr_min)
    return curr_min, curr_max


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)


# Regular test cases

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 100)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 99) == get_min_max(l)) else "Fail")

l = [i for i in range(-100, 100)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((-100, 99) == get_min_max(l)) else "Fail")



# Edge test cases

print(get_min_max([])) # Empty list

print(get_min_max([1])) # One element
