"""
Write a function, get_node_value, that takes in the head of a linked list and an index.
The function should return the value of the linked list at the specified index.
If there is no node at the given index, then return None.
"""

from node import Node

def get_node_value[T](head: Node[T], index: int) -> T | None:
    current_node = head
    current_index = 0

    while current_node is not None:
        if current_index == index:
            return current_node.value

        current_node = current_node.next
        current_index += 1

    return None

"""
Analysis:
Time complexity: O(n)
Space complexity: O(1)
"""