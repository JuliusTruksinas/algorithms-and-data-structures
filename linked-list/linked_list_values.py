"""
Write a function, linked_list_values, that takes in the head of a linked list as an argument.
The function should return a list containing all values of the nodes in the linked list.
"""

class Node[T]:
    def __init__(self, value: T):
        self.value = value
        self.next: Node[T] | None = None

def linked_list_values[T](head: Node[T]) -> list[T]:
    current = head
    result: list[T] = []

    while current is not None:
        result.append(current.value)
        current = current.next
    
    return result