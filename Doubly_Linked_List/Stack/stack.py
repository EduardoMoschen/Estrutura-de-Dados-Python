class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None


class Stack:
    def __init__(self) -> None:
        self.head = None
        self.last = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.previous = self.last
        if self.head is None and self.last is None:
            self.head = new_node
            self.last = new_node
        else:
            self.head.previous = new_node
            self.head = new_node
        self.size += 1

    def pop(self):
        if self.head is None and self.last is None:
            raise ValueError("Stack is empty")
        else:
            popped = self.head
            self.head = self.head.next
            if self.head is not None:
                self.head.previous = None
            else:
                self.head = None
                self.last = None
        self.size -= 1
        return popped.data

    def print_stack(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
