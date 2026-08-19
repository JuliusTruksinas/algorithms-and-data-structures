"""
Write a function, palindrome, that takes in a string and returns a boolean indicating whether or not the string is the same forwards and backwards.
You must solve this recursively.
"""

def palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])

"""
Analysis:
Time complexity: O(n^2)
Space complexity: O(n^2)
"""