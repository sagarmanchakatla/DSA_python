# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ls1 = []
        ls2 = []

        while l1 and l1.next is not None:
            ls1.append(l1.val)
            l1 = l1.next
        if l1:
            ls1.append(l1.val)

        while l2 and l2.next is not None:
            ls2.append(l2.val)
            l2 = l2.next
        if l2:
            ls2.append(l2.val)

        n1, n2 = 0, 0
        for i in range(len(ls1),0,-1):
            n1 = n1*10 + ls1[i-1]
        for i in range(len(ls2),0,-1):
            n2 = n2*10 +ls2[i-1]

        a = str(n1+n2)
        ans = []

        for i in range(len(a),0,-1):
            ans.append(int(a[i-1]))

        dummy_head = ListNode(0)
        current = dummy_head
        for value in ans:
            current.next = ListNode(value)
            current = current.next

        return dummy_head.next

    def optimal(self, l1, l2):
        dummy_head = ListNode(-1)
        curr = dummy_head
        carry = 0

        while l1 or l2:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            new_node = ListNode(sum % 10)
            curr.next = new_node
            curr = curr.next

        return dummy_head.next