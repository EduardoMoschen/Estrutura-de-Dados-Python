from queue import Queue


def main():

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.print_queue()
    queue.dequeue()
    queue.dequeue()
    print()
    queue.print_queue()


if __name__ == "__main__":
    main()
