"""
Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument.
The function should return the total sum of all values in the linked list.
"""

from node import Node

def sum_list(head: Node[int]):
    result: int = 0
    current: Node[int] | None = head

    while current is not None:
        result += current.value
        current = current.next

    return result

"""
Analysis:
Time complexity: O(n)
Space complexity: O(1)
"""
