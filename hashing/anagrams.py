"""
Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.
"""

def get_char_count(word: str) -> dict[str, int]:
    result = {}

    for char in word:
        result[char] = result.get(char, 0) + 1

    return result

def anagrams(s1: str, s2: str) -> bool:
    return get_char_count(s1) == get_char_count(s2)

"""
Analysis:
Time Complexity: O(n+m) - Linear
Space Complexity: O(n+m) - Linear

Lessons learnt:
1. when you compare python dicts they are compared based on the value (not by reference)
"""