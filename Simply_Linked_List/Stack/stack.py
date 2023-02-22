class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise ValueError("Stack is empty")
        temp = self.head
        self.head = temp.next
        popped = temp.data
        self.size -= 1
        return popped

    def print_stack(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
