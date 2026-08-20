class Node[T]:
    def __init__(self, value: T):
        self.value = value
        self.next: Node[T] | None = None

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d

def print_list[T](head: Node[T]) -> None:
    current = head

    while current is not None:
        print(current.value)
        current = current.next

def print_list_recursive[T](head: Node[T] | None) -> None:
    if head is None:
        return

    print(head.value)

    print_list_recursive(head.next)

print_list(a)
print_list_recursive(a)