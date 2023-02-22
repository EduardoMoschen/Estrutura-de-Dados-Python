from stack import Stack


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.print_stack()

    stack.pop()
    stack.pop()
    print()
    stack.print_stack()


if __name__ == "__main__":
    main()
