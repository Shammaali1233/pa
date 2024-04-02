class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Sorted linkedlist - sorted by the date.
class SortedLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, value):
        new_node = Node(value)
        if self.head is None or value.date < self.head.value.date:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.value.date < value.date:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def get(self, index):
        current = self.head
        count = 0
        while current is not None and count < index:
            current = current.next
            count += 1
        if current is None:
            raise IndexError("Index out of range")
        return current.value

    def get_size(self):
        return self.size
