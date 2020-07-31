"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from .stack import Stack
from .queue import Queue


class BSTNode(object):
    """Binary search tree node."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            return False if self.left is None else self.left.contains(target)
        else:
            return False if self.right is None else self.right.contains(target)

    def get_max(self):
        return self.value if self.right is None else self.right.get_max()

    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
    
    @property
    def in_order_print(self):
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)

    @staticmethod
    def bft_print(node):
        queue = Queue()
        queue.enqueue(node)
        while queue.size > 0:
            current_node = queue.dequeue()
            print(current_node.value)
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

    @staticmethod
    def dft_print(node):
        stack = Stack()
        stack.push(node)
        while stack.size > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)

    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)
