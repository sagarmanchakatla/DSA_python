class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_pos(self, pos, val):
        new_node = Node(val)
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next

    def display(self):
        if not self.head:
            print('List is empty')

        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next


li = DoublyLinkedList()

li.insert_at_pos(2, 100)
li.display()

