"""
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:
"""

# This function is the first attempt to the question. Time complexity: O(n*n)
def sqrt_quadratic_complexity(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0:
        return 0

    ans = 1

    for i in range(1, number):
        if i * i <= number:
            sqrt = i
        else:
            break
    return ans

    pass


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        print("Please enter a non-negative number")
        return

    if number == 0 or number == 1:
        return number

    mid = number // 2
    low = 0
    high = number - 1

    while low <= high:
        mid = (low + high) // 2
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1

    return ans


# Regular test cases
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Edge test cases
print(sqrt(-1))
print ("Pass" if  (0 == sqrt(0)) else "Fail")
