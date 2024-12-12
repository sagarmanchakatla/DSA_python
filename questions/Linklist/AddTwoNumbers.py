class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ls1 = []
        ls2 = []

        while l1.next is not None:
            ls1.append(l1.val)
            l1 = l1.next
        ls1.append(l1.val)

        while l2.next is not None:
            ls2.append(l2.val)
            l2 = l2.next
        ls2.append(l2.val)



        n1, n2 = 0, 0
        for i in range(len(ls1), 0, -1):
            n1 = n1*10 + ls1[i-1]
        for i in range(len(ls2), 0, -1):
            n2 = n2*10 + ls2[i-1]

        a = str(n1+n2)
        ans = []

        for i in range(len(a),0,-1):
            ans.append(int(a[i-1]))

        dummy_head = ListNode(0)
        current = dummy_head
        for value in ans:
            current.next = ListNode(value)
            current = current.next

        print(dummy_head.next)
        

        # print(ans)
        # print(n1)
        # print(n2)
        # print(ls1)
        # print(ls2)
    


# Helper function to create a linked list from a list.
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Test the addTwoNumbers function
if __name__ == "__main__":
    # Create two linked lists for testing
    l1 = create_linked_list([2, 4, 3])  # Represents the number 342
    l2 = create_linked_list([5, 6, 4])  # Represents the number 465

    # Instantiate the Solution class and test the method
    solution = Solution()
    solution.addTwoNumbers(l1, l2)