# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. Recursive Postorder Traversal
class Solution:
    def visit(self, node, n_list):
        if node is None:
            return
        self.visit(node.left, n_list)
        self.visit(node.right, n_list)
        n_list.append(node.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        n_list = []
        self.visit(root, n_list)
        return n_list

# 2.1 Iterative Postorder Traversal---Based on preorder, then reverse
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res_list = []
        stack = [root]
        while stack:
            node = stack.pop()
            res_list.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res_list[::-1]

# 2.2 Iterative Postorder Traversal---Stack + Visited State
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res_list = []
        stack = [(root, 0)]
        while stack:
            node, visited = stack.pop()
            if visited:
                res_list.append(node.val)
            else:
                stack.append((node, 1))
                if node.right:
                    stack.append((node.right, 0))
                if node.left:
                    stack.append((node.left, 0))

        return res_list

# 2.3 Iterative Postorder Traversal (More To Do)
