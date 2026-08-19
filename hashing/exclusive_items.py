"""
Write a function, exclusive_items, that takes in two lists, a,b, as arguments.
The function should return a new list containing elements that are in either list but not both lists.
You may assume that each input list does not contain duplicate elements.
"""

def exclusive_items(a: list[int], b: list[int]) -> list[int]:
    a_set = set(a)
    b_set = set(b)
    result: list[int] = []

    for a_element in a:
        if a_element not in b_set:
            result.append(a_element)

    for b_element in b:
        if b_element not in a_set:
            result.append(b_element)

    return result

"""
Analysis:
Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""