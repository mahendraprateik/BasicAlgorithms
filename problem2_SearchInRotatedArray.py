"""
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with:
"""

def rotated_array_search(arr, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(arr) == 0:
        return "Array is empty"

    start = 0
    end = len(arr) - 1

    if arr[start] == arr[end] or arr[start] <= arr[end]:
        print("Array is sorted")
        return

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == number:
            return mid
        elif arr[start] <= arr[mid]:
            if number >= arr[start] and number < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if number >= arr[mid] and number <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    print("searching for: ", test_case[1])
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Regular test cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Edge test cases
print(rotated_array_search([], 10)) # should print "Array is empty"
