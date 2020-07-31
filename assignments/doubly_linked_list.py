class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        else:
            self.head = new_node
            self.tail = new_node

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        if self.tail:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        else:
            self.head = new_node
            self.tail = new_node

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    def move_to_front(self, node):
        if node is self.head:
            return
        self.add_to_head(node.value)
        self.delete(node)

    def move_to_end(self, node):
        if node is self.tail:
            return
        self.add_to_tail(node.value)
        self.delete(node)

    def delete(self, node):
        if not self.head:
            print("Empty")
            return
        self.length -= 1

        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.delete()

    def get_max(self):
        if self.head is None:
            return "Empty list"
        elif self.head == self.tail:
            return self.head.value
        else:
            self.node_values = []
            for items in range(self.length):
                self.number = self.head.next.value
                self.node_values.append(self.number)
            self.node_values.append(self.head.value)
            self.node_values.append(self.tail.value)
            return max(self.node_values)
