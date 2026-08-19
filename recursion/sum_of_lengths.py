"""
Write a function sumOfLengths that takes in a list of strings and returns the total length of the strings.
You must solve this recursively.

"""

def sum_of_lengths(strings: list[str]):
    if len(strings) == 0:
        return 0

    return len(strings[0]) + sum_of_lengths(strings[1:])


"""
Analysis:
Time Complexity: O(n^2)
    - number of function calls = n
    - in each function call we perform list slicing = O(n)

Space Complexity: O(n^2)
    - number of function calls = n
    - in each function call we store a sub array of strings = O(n)
"""