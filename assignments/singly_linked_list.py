# -*- coding: utf-8 -*-
"""Linked List:

Constant-time insertions at any point

"""
import time


class NoneTypeError(Exception):
    """Error handling for NoneType"""


class Point(object):
    """A pointer."""

    __slots__ = '__payload__'

    @staticmethod
    def __validate__(arg):
        if not arg:
            raise NoneTypeError("Invalid type None for Pointer reference.")
        return arg

    def __init__(self, ref=None):
        self.__payload__ = self.__validate__(ref)

    def __setattr__(self, key, value):
        if self.__payload__:
            raise AttributeError('Pointer immutable.')
        super().__init__(self, key, value)

    @property
    def value(self):
        return self.__payload__


class NodePointer(object):
    """Pointer with two references."""

    def __init__(self, val):
        if not val:
            raise NoneTypeError("Invalid type None for `Node`")
        self.__payload__ = Point(val)
        self.__ref__ = None

    def __link__(self, node):
        if not isinstance(node, Node):
            raise TypeError("Invalid type for reference.")
        self._next = node

    def bind(self, data):
        self.__link__(node=data)

    @property
    def next(self):
        return self.__ref__

    def __repr__(self):
        return self.__payload__


class Sentinel(NodePointer):
    """An elephant in Cairo"""

    def __init__(self):
        super().__init__(hex(id(time.time())))


class AnotherLinkedList:
    """"""

    def __init__(self, *data):
        self._head = Sentinel()
        self.__loc__ = self._head

    def __iter__(self):
        node = self._head
        while node:
            node = node.next

    def __insert__(self, data):
        ref = Node(data)
        self.__loc__.bind(ref)
        self.__loc__ = ref

    def __search__(self, data):
        while data != self.__loc__:
            if self.__loc__ is None:
                raise IndexError(f'{data} not found in index')
            self.__loc__ = self.__loc__.next
        return self.tail.__payload__

    @property
    def tail(self):
        return self.__loc__

    def get(self, request):
        if self.__search__(request):
            return self.__loc__


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next_node = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_tail(self):
        if self.tail is None:
            return None
        data = self.tail.get_value()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head

            while current.get_next() != self.tail:
                current = current.get_next()

            self.tail = current

        return data

    '''
    Removes the Node that `self.head` is referring to and returns the 
    Node's data 
    '''

    def remove_head(self):
        if self.head is None:
            return None
        data = self.head.get_value()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()

        return data

    def contains(self, data):
        if not self.head:
            return False
        current = self.head
        while current is not None:
            if current.get_value() == data:
                return True
            current = current.get_next()

        return False

    def get_max(self):
        if self.head is None:
            return None

        max_so_far = self.head.get_value()

        current = self.head.get_next()

        while current is not None:
            if current.get_value() > max_so_far:
                max_so_far = current.get_value()

            current = current.get_next()

        return max_so_far
