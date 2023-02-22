from doubly import DoublyLinkedList


def main():
    doubly_linked = DoublyLinkedList()
    doubly_linked.insert_end(1)
    doubly_linked.insert_end(2)
    doubly_linked.insert_end(4)
    doubly_linked.insert_end(5)
    doubly_linked.insert_start(0)
    doubly_linked.insert_in_order(3)
    doubly_linked.print_list()
    doubly_linked.remove_end()
    doubly_linked.remove_start()
    doubly_linked.remove(3)
    print()
    doubly_linked.print_list()


if __name__ == "__main__":
    main()
