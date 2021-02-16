"""
Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:
"""

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if len(input_list) == 0:
    	return

    i = 0
    j = len(input_list) - 1
    k = 0

    while k <= j:
    	if input_list[k] == 0:
    		input_list[k], input_list[i] = input_list[i], input_list[k]
    		k += 1
    		i += 1
    	elif input_list[k] == 2:
    		input_list[j], input_list[k] = input_list[k], input_list[j]
    		j -= 1
    	else:
    		k += 1

    return input_list
    pass

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Regular test cases

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Edge test cases

print(sort_012([])) # Empty arrat
print(sort_012([2, 1, 0])) # Should return [0, 1, 2]
print(sort_012([1])) # Should return [1]