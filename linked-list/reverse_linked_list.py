"""
Write a function, reverse_list, that takes in the head of a linked list as an argument.
The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.
"""

from node import Node

def reverse_list[T](head: Node[T]) -> Node[T]:
    current_node: Node[T] | None = head
    previous_node: Node[T] | None = None

    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    if previous_node is None:
        raise RuntimeError("Reverse linked list impossible case")

    return previous_node

"""
Analysis:
Time complexity: O(n)
Space complexity: O(1)
"""

def reverse_list_recursive[T](head: Node[T] | None, previous: Node[T] | None = None) -> Node[T]:
    if head is None:
        if previous is None:
            raise RuntimeError("Reverse linked list impossible case")

        return previous
    
    next = head.next
    head.next = previous

    return reverse_list_recursive(next, head)

"""
Analysis:
Time complexity: O(n)
Space complexity: O(n)
"""