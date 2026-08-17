"""
Write a function, most_frequent_char, that takes in a string as an argument.
The function should return the most frequent character of the string.
If there are ties, return the character that appears earlier in the string.
You can assume that the input string is non-empty.
"""

def most_frequent_char(s: str) -> str:
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    result = s[0]

    for char in s:
        if char_count[char] > char_count[result]:
            result = char

    return result

"""
Analysis:
Time Complexity: O(n)
Space Complexity: O(n)
"""



