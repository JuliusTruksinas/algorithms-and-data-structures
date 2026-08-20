class Node[T]:
    def __init__(self, value: T):
        self.value = value
        self.next: Node[T] | None = None