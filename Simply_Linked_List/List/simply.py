
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None  # Referência para o próximo nó é nula.


class LinkedList:
    def __init__(self) -> None:
        # head será usado como ponto de referência dentro da lista.
        self.head = None
        # size será necessário para quando quisermos dividir a lista
        # para algumas operações, como ordenação.
        self.size = 0

    def insert_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
        self.size += 1

    def insert_in_order(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.data < data and current_node.next:
                current_node = current_node.next
            if current_node.data < data:
                current_node.next = new_node
            else:
                new_node.next = current_node
                self.head = new_node
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
            raise ValueError("List is empty")
        self.head = self.head.next
        self.size -= 1

    def remove_end(self):
        temp = self.head
        if temp is None:
            raise ValueError("List is empty")
        while temp.next is not None:
            previous = temp
            temp = temp.next
        if previous is not None:
            previous.next = None
        self.size -= 1

    def remove(self, data):
        temp = self.head
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                self.size -= 1
                return
        while temp is not None:
            if temp.data == data:
                break
            previous = temp
            temp = temp.next
            if temp is None:
                return
            previous.next = temp.next
            self.size -= 1
            temp = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
