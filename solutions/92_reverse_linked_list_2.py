# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        cnt = -1
        mid_first = None
        mid_head = None
        mid_tail = None
        while p:
            cnt += 1
            if cnt == m - 1:
                mid_first = p
                p = p.next
            elif cnt == m:
                mid_head = ListNode(0)
                mid_head.next = p
                p = p.next
                mid_head.next.next = None
                mid_tail = mid_head.next
            elif cnt > m and cnt <= n:
                tmp_p = p
                p = p.next
                tmp_p.next = mid_head.next
                mid_head.next = tmp_p
                if cnt == n:
                    break
            else:
                p = p.next
        mid_first.next = mid_head.next
        mid_tail.next = p
        return dummy.next


