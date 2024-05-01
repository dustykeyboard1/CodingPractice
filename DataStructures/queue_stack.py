"""
Implementation of a queue (First in First out)
"""


class Node:
    def __init__(self, value: int) -> None:
        self.data = value
        self.next = None


class myqueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add(self, value):
        new = Node(value)
        if self.tail != None:
            self.tail.next = new
        self.tail = new
        if self.head == None:
            self.head = new

    def remove(self):
        data = None
        if self.head != None:
            data = self.head.data
            self.head = self.head.next
        if self.head == None:
            self.tail = None
        return data


class Stack:
    def __init__(self) -> None:
        self.head = None

    def add(self, data):
        new = Node(data)
        if self.head != None:
            old = self.head
            self.head = new
            self.head.next = old
        else:
            self.head = new

    def remove(self):
        if self.head != None:
            data = self.head.data
            self.head = self.head.next
            return data
        else:
            return None


def main():
    mq = myqueue()
    mq.add(10)
    mq.add(15)
    mq.add(20)
    print(mq.remove())
    mq.add(25)
    print(mq.remove())
    print()
    data = mq.remove()
    while data != None:
        print(data)
        data = mq.remove()

    print()
    mq.add(10)
    mq.add(15)
    mq.add(20)
    data = mq.remove()
    while data != None:
        print(data)
        data = mq.remove()

    print("-------------------------------------------")

    mq = Stack()
    mq.add(10)
    mq.add(15)
    mq.add(20)
    print(mq.remove())
    mq.add(25)
    print(mq.remove())
    print()
    data = mq.remove()
    while data != None:
        print(data)
        data = mq.remove()

    print()
    mq.add(10)
    mq.add(15)
    mq.add(20)
    data = mq.remove()
    while data != None:
        print(data)
        data = mq.remove()


if __name__ == "__main__":
    main()
