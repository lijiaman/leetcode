## Essentially preorder traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        dummy = TreeNode(0)
        prev_node = dummy
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            prev_node.right = node
            prev_node.left = None

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            prev_node = node

        return dummy.right