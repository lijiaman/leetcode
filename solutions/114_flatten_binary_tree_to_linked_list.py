# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. Stack
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
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

# 2. Recursive Solution
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root

# 3. Iterative Solution, O(1) space (*)
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        while root:
            if root.left:
                node = root.left
                while node.right:
                    node = node.right
                node.right = root.right
                root.right = root.left
                root.left = None
            root = root.right


