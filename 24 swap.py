class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode(None)
        while head and head.next:
            nexth = head.next.next
            prev.next = head.next
            head.next.next = head
            prev = head
            head = nexth
        prev.next = head
        return dummy.next
