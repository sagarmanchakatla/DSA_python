# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def brute(self, head, n):
        if not head:
            return head

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        if n == count:
            newHead = head.next
            return newHead

        res = count - n
        curr = head
        while curr:
            res -= 1
            if res == 0:
                break
            curr = curr.next

        curr.next = curr.next.next
        return head

    def optimal(self, head, n):
        if not head:
            return None

        fast = head
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        slow = head

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head

