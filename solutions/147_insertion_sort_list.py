# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Insertion Sort for Linked List
# 0. My original ugly solution (totally followed the graphical illustration...)
# 1536ms(48.30%), 15.1M(39.30%)
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        p = dummy
        p.next = head
        head = head.next
        p.next.next = None
        while head:
            p_in = dummy.next
            prev = dummy
            insert_flag = False
            while p_in:
                if head.val > p_in.val:
                    prev.next = head
                    tmp = head
                    head = head.next
                    tmp.next = p_in
                    insert_flag = True
                    break
                prev = p_in
                p_in = p_in.next
            if not insert_flag:
                prev.next = head
                head = head.next
                prev.next.next = None

        r_dummy = ListNode(0)
        p = dummy.next
        while p:
            tmp_p = p
            p = p.next
            tmp_p.next = r_dummy.next
            r_dummy.next = tmp_p

        return r_dummy.next

# 1. Sorting in a Linked List Way, one-pass
# 172ms(83.32%), 15.1M(37.60%)
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        p_cmp = dummy
        dummy.next = head
        p = head
        while p and p.next:
            if p.val < p.next.val:
                p = p.next
                continue
            if p_cmp.next.val > p.next.val:
                p_cmp = dummy
            while p_cmp.next.val < p.next.val:
                p_cmp = p_cmp.next
            tmp_p = p.next
            p.next = tmp_p.next
            tmp_p.next = p_cmp.next
            p_cmp.next = tmp_p

        return dummy.next











