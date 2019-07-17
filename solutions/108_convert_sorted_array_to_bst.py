# Notice that the edge value index really matters a lot!

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive Solution
class Solution(object):
    def build(self, num_list, low, high):
        if low == high:
            return
        mid = (low + high) // 2
        node = TreeNode(num_list[mid])
        node.left = self.build(num_list, low, mid)
        node.right = self.build(num_list, mid + 1, high)

        return node


    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.build(nums, 0, len(nums))