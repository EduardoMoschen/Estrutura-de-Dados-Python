class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.last = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.last = new_node
        else:
            new_node.previous = self.last
            self.last.next = new_node
            self.last = new_node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            raise ValueError("Queue is empty")
        else:
            dequeued = self.head.next
            self.head = self.head.next
            if self.head is not None:
                self.head.previous = None
            self.size -= 1
            return dequeued

    def print_queue(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
