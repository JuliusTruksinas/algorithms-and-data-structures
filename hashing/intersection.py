"""
Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.
"""

def intersection(a: list[int], b: list[int]) -> list[int]:
    items_set = set(a)

    result: list[int] = []

    for el in b:
        if el in items_set:
            result.append(el)

    return result

"""
Analysis:
Time Complexity: O(n+m)
Space Complexity: O(n)
"""