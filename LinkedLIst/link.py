class Node:
    def __init__(self, data, next= None):
        self.val = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return 
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        print('Node inserted at end')
    
    def insert_at_begining(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        print('Node inserted at Begining')
        
    def insert_at_pos(self, val, pos):
        new_node = Node(val)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            print('Node inserted at Begining')
            
        if not self.head:
            print('List empty')
            return
    
        curr = self.head
        # while 
    
    def delete_at_end(self):
        if not self.head:
            print('List is empty')
            return
        
        if not self.head.next: 
            self.head = None
            print('Deleted at end')
            return
        
        curr = self.head
        while curr.next.next:
            curr = curr.next
        
        curr.next = None
        print('Deleted at end')
    
    def delete_at_beg(self):
        if not self.head:
            print('List empty')
            return 
        self.head = self.head.next
        print('Deleted at begining')
    
    def display(self):
        if not self.head:
            print('List empty')
            return
        
        curr = self.head
        while curr:
            print(curr.val, end='->')
            curr = curr.next
        print('None')
        

if __name__ == '__main__':
    li = LinkedList()
    
    li.insert_at_begining(10)
    li.insert_at_begining(20)
    li.insert_at_begining(30)
    li.insert_at_begining(40)
    
    li.delete_at_end()
    li.display()