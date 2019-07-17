# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. Recursive, top-down approach
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        next_p = slow.next
        slow.next = None
        mid_node = TreeNode(next_p.val)

        mid_node.left = self.sortedListToBST(head)
        mid_node.right = self.sortedListToBST(next_p.next)

        return mid_node

# 2. Recursive, bottom-up approach(To Do)

# 3. Convert to array for building tree(To Do)
