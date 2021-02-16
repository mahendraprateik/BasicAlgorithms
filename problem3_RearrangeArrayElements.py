"""
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
"""
def merge_sort(array):
	if len(array) == 0:
		return
	if len(array) == 1:
		return array

	mid = len(array) // 2

	left_sorted = merge_sort(array[:mid])
	right_sorted = merge_sort(array[mid:])

	return merge(left_sorted, right_sorted)

def merge(left_array, right_array):

	if len(left_array) == 0:
		return right_array
	if len(right_array) == 0:
		return left_array

	merged = []
	left_index = 0
	right_index = 0

	while left_index < len(left_array) and right_index < len(right_array):
		if left_array[left_index] >= right_array[right_index]:
			merged.append(right_array[right_index])
			right_index += 1
		else:
			merged.append(left_array[left_index])
			left_index += 1

	merged += left_array[left_index:]
	merged += right_array[right_index:]

	return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_array = merge_sort(input_list)

    if not sorted_array:
        return
    num1 = 0
    num2 = 0

    index = 0
    left_factor = 0
    right_factor = 0

    for index in range(len(sorted_array)):
    	if index % 2 == 0:
            num1 += 10 ** left_factor * sorted_array[index]
            left_factor += 1
    	else:
            num2 += 10 ** right_factor * sorted_array[index]
            right_factor += 1
    print(num1, num2)
    return [num1, num2]
    
    pass

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Regular test cases

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 3, 5, 7, 4, 6], [753, 641]])

# Edge cases
print(rearrange_digits([])) # Empty array
test_function([[1], [1]])
