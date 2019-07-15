# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev_node = dummy
        p = head
        data_dict = {}
        while p:
            curr_val = p.val
            if curr_val not in data_dict:
                data_dict[curr_val] = prev_node
                prev_node = p
                p = p.next
            else:
                while p and p.val == curr_val:
                    p = p.next
                data_dict[curr_val].next = p
                prev_node = data_dict[curr_val]

        return dummy.next



