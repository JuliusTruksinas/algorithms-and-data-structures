"""
Write a function, reverse_string, that takes in a string as an argument.
The function should return the string with its characters in reverse order. You must do this recursively.
"""

def reverse_string(s: str):
    if(len(s) == 0):
        return ""

    return reverse_string(s[1:]) + s[0]

"""
Analysis:
Time complexity: O(n^2)
    - number of function calls = n
    - in each function call we perform string slicing = O(n)

Space complexity: O(n^2)
    - number of function calls = n
    - each function call stores the string lenght n
"""