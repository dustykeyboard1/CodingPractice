"""
Binary search tree implmentation    
"""


class Node:
    def __init__(self, data: int):
        self.value = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def recur_insert(self, root, node):
        if root.value > node.value:
            if root.left == None:
                root.left = node
            else:
                self.recur_insert(root.left, node)

        else:
            if root.right == None:
                root.right = node
            else:
                self.recur_insert(root.right, node)

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.recur_insert(self.root, Node(value))

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(" " * 4 * level + "->", node.value)
            self.print_tree(node.left, level + 1)


def main():
    bst = BST()
    bst.insert(10)
    bst.insert(20)
    bst.insert(30)
    bst.insert(40)
    bst.insert(50)
    bst.insert(60)
    bst.insert(5)
    bst.insert(6)
    bst.insert(11)
    bst.print_tree(bst.root)


if __name__ == "__main__":
    main()
