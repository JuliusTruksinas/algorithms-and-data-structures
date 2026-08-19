"""
Write a function, intersection_with_dupes, that takes in two lists, a,b, as arguments.
The function should return a new list containing elements that are common to both input lists. The elements in the result should appear as many times as they occur in both input lists.
You can return the result in any order.
"""

def intersection_with_dupes(a: list[str], b: list[str]) -> list[str]:
    a_items_count: dict[str, int] = {}
    for a_element in a:
        a_items_count[a_element] = a_items_count.get(a_element, 0) + 1

    b_items_count = {}
    for b_element in b:
        b_items_count[b_element] = b_items_count.get(b_element, 0) + 1

    result: list[str] = []

    for a_element, count in a_items_count.items():
        if a_element not in b_items_count:
            continue

        result.extend([a_element] * min(count, b_items_count[a_element]))

    return result

"""
Analysis:
Time Complexity:
Space Complexity:
"""