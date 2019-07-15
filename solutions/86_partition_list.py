# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode(0)
        big = ListNode(0)
        p_small = small
        p_big = big
        p = head
        while p:
            if p.val < x:
                p_small.next = p
                p_small = p_small.next
            elif p.val >= x:
                p_big.next = p
                p_big = p_big.next
            p = p.next

        p_small.next = big.next
        p_big.next = None
        return small.next