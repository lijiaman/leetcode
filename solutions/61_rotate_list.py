# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        p = head
        cnt = 1
        while True:
            p = p.next
            cnt += 1
            if p.next is None:
                p.next = head
                break

        len_list = cnt
        k = k % len_list
        d_p = head
        cnt = 1
        while True:
            if cnt == len_list - k:
                head = d_p.next
                d_p.next = None
                break
            d_p = d_p.next
            cnt += 1

        return head