class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def insert_start(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.previous = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.previous = new_node
            new_node.next = self.head
            new_node.previous = None
            self.head = new_node
        self.size += 1

    def insert_end(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.previous = None
            self.head = new_node
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.previous = current_node
            new_node.next = None
        self.size += 1

    def insert_in_order(self, data):
        new_node = Node(data)
        current_node = self.head
        if current_node is None:
            new_node.next = self.head
            new_node.previous = None
            self.head = new_node
        else:
            while current_node.data < data and current_node.next:
                current_node = current_node.next
            if current_node.data < data:
                current_node.next = new_node
                new_node.previous = current_node
                new_node.next = None
            else:
                new_node.next = current_node
                new_node.previous = current_node.previous
                if current_node.previous:
                    current_node.previous.next = new_node
                else:
                    self.head = new_node
                current_node.previous = new_node
        self.size += 1

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return f"Data {data} founded!"
            current_node = current_node.next
        return f"Data {data} not founded!"

    def remove_start(self):
        if self.head is None:
            raise ValueError("Queue is empty")
        current_node = self.head
        self.head = current_node.next
        current_node.next.previous = None
        self.size -= 1

    def remove_end(self):
        if self.head is None:
            raise ValueError("Queue is empty")
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.previous.next = None
        self.size -= 1

    def remove(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node == self.head:
                    self.head = current_node.next
                    current_node.next.previous = None
                    current_node = None
                    self.size -= 1
                    return
                else:
                    current_node.previous.next = current_node.next
                    current_node.next.previous = current_node.previous
                    current_node = None
                    self.size -= 1
                    return
            current_node = current_node.next
        return f"Node {data} not founded!"

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
