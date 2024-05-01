"""
Implement a node and linked list class to create a linked list. 
"""


class Node:
    def __init__(self, value: int) -> None:
        self.node_value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new: int) -> None:
        if self.head == None:
            self.head = Node(new)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(new)

    def prepend(self, new: int) -> None:
        if self.head == None:
            self.head = Node(new)
            self.head.next = None
        else:
            new = Node(new)
            new.next = self.head
            self.head = new

    def delete(self, value: int) -> None:
        current = self.head
        while current.next.node_value != value:
            current = current.next
        current.next = current.next.next

    def print(self) -> None:
        current = self.head
        print(current.node_value)
        while current.next != None:
            current = current.next
            print(current.node_value)

    def insert(self, value: int, index: int) -> None:
        current = self.head
        for i in range(index - 1):
            if current.next != None:
                current = current.next
            else:
                self.append(value)
        new = Node(value)
        new.next = current.next
        current.next = new


def main():
    myLL = LinkedList()
    for item in [1, 2, 3, 4, 5, 6, 7]:
        myLL.append(item)

    myLL.prepend(9)
    for item in [10, 11, 12, 13]:
        myLL.append(item)
    myLL.prepend(100)
    myLL.delete(4)
    myLL.delete(6)
    myLL.insert(86, 4)
    myLL.print()


if __name__ == "__main__":
    main()
