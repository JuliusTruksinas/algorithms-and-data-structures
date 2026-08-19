"""
Write a function sum_numbers_recursive that takes in an array of numbers and returns the sum of all the numbers in the array.
All elements will be integers. Solve this recursively.
"""

def sum_numbers_recursive(numbers: list[int]):
    if len(numbers) == 0:
        return 0

    return numbers[0] + sum_numbers_recursive(numbers[1:])

"""
Analysis:
Number of function calls: O(n+1) = O(n)
Array slicing time complexity for each function call: O(n)
Total Time complexity: O(n^2)

Each function call takes up space: O(n+1) = O(n)
Within each function call we store the sliced array = O(n)
Total Space complexity: O(n^2)
"""