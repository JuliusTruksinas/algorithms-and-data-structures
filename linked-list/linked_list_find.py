"""
Write a function, linked_list_find, that takes in the head of a linked list and a target value.
The function should return a boolean indicating whether or not the linked list contains the target.
"""

from node import Node

def linked_list_find[T](head: Node[T], target: T) -> bool:
    current = head

    while current is not None:
        if current.value == target:
            return True

        current = current.next

    return False

"""
Analysis:
Time complexity: O(n)
Space complexity: O(1)
"""
