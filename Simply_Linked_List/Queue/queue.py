class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.last = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.last is None:
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            raise ValueError("Queue is empty")
        temp = self.head
        self.head = temp.next
        dequeued = temp.data
        self.size -= 1
        return dequeued

    def print_queue(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
