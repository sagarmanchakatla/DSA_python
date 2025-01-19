from Tools.scripts.generate_opcode_h import header


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_end(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            # print('List empty, inserted at end')
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            # print('Inserted at the end')

    def insert_at_beg(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
            # print('List empty, inserted at beg')
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_position(self, pos, val):
        new_node = Node(val)
        if pos == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            # print(f'Node inserted at pos: {pos}')
            return

        curr = self.head
        count = 0

        while curr and count < pos:
            if count == pos - 1:
                new_node.next = curr.next
                curr.next.prev = new_node
                curr.next = new_node
                new_node.prev = curr
                # print(f'Node inserted at pos:{pos}')
                return
            count += 1
            curr = curr.next

        # print('invalid pos')

    def delete_at_pos(self, pos):
        if not self.head or pos < 0:
            # print('List empty')
            return

        curr = self.head
        if pos == 0:
            if self.head:
                self.head.prev = None
                self.head = self.head.next
                return self.head

        count = 0
        while curr and count < pos:
            curr = curr.next
            count += 1

        if curr:
            if curr.next:
                curr.next.prev = curr.prev
                curr.prev.next = curr.next
                return self.head
        else:
            print('Positions exceed')


    def reverse(self):
        if not self.head:
            # print('List empty')
            return None

        curr = self.head
        self.tail = None

        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            self.head = curr
            curr = curr.prev

        # self.head = new_head


    def display(self):
        if not self.head:
            print('List empty')
            return
        curr = self.head

        while curr:
            print(curr.data, end=' -> ')
            curr = curr.next

if __name__ == '__main__':
    li = DoublyLinkedList()

    li.insert_at_end(100)
    li.insert_at_end(200)
    li.insert_at_end(300)
    li.insert_at_end(400)
    li.insert_at_beg(50)
    li.reverse()
    # li.insert_at_position(2, 500)
    # li.delete_at_pos(2)
    li.display()
