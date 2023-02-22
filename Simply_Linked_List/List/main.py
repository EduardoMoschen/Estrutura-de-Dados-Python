from simply import LinkedList


def main():
    linked_list = LinkedList()
    linked_list.insert_end(2)
    linked_list.insert_end(4)
    linked_list.insert_end(172)
    linked_list.insert_start(8)
    linked_list.insert_start(10)

    # linked_list.insert_in_order(2)
    # linked_list.insert_in_order(4)
    # linked_list.insert_in_order(6)
    # linked_list.insert_in_order(8)
    # linked_list.insert_in_order(10)
    linked_list.print_list()
    linked_list.remove_end()
    print()
    linked_list.remove_start()
    linked_list.remove(172)
    linked_list.print_list()

    # print(linked_list.search(8))


if __name__ == "__main__":
    main()
