# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 0. My original solution using dictionary for storing index of nodes
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        data_dict = {}
        cnt = 0
        p = head
        while p:
            data_dict[cnt] = p
            p = p.next
            cnt += 1

        for i in range(cnt // 2):
            if cnt - 2 - i >= 0:
                curr_node = data_dict[i]
                prev_last_node = data_dict[cnt - 2 - i]
                last_node = data_dict[cnt - 1 - i]
                prev_last_node.next = None
                last_node.next = curr_node.next
                curr_node.next = last_node

# 1. Linked List, Split and Merge
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            left_s = head
            right_s = slow.next
            slow.next = None

            pre = None
            right_p = right_s
            while right_p:
                right_p.next, pre, right_p = pre, right_p, right_p.next

            l_p = left_s
            r_p = pre
            while l_p and r_p:
                l_p.next, r_p.next, l_p, r_p = r_p, l_p.next, l_p.next, r_p.next










