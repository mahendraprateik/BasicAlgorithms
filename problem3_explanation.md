# Problem 3: Rearrange Array Elements

## Method and Data Structures:
We first need to sort the array and then use a logic go through the sorted array from minimum to maximum and assign it to two numbers alteratively fillng
their 0th, 10th, 100th and so on

## Worst case time complexity is: <b> O(n log n) </b>
Merge sort -> O (n log n)
Traversing through sorted array to create a number -> O (n)

## Worst case space complexity is: <b> O(2) </b>
Since we are returning 2 numbers
