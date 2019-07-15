# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Merge Sort
# 236ms(59.70%), 20.7M(57.14%)
class Solution:
    def merge(self, l_node, r_node):
        dummy = ListNode(0)
        p = dummy
        while l_node and r_node:
            if l_node.val <= r_node.val:
                p.next = l_node
                l_node = l_node.next
            else:
                p.next = r_node
                r_node = r_node.next
            p = p.next

        p.next = l_node or r_node
        return dummy.next

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None
        l = self.sortList(head)
        r = self.sortList(slow)
        return self.merge(l, r)