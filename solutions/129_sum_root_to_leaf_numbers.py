# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. DFS Recursively
class Solution:
    def traversal(self, node, depth, sum, sum_list):
        if node:
            sum = sum * 10 + node.val
        if (not node.left) and (not node.right):
            sum_list.append(sum)
            return
        if node.left:
            self.traversal(node.left, depth + 1, sum, sum_list)
        if node.right:
            self.traversal(node.right, depth + 1, sum, sum_list)

    def sumNumbers(self, root: TreeNode) -> int:
        sum_list = []
        if root is None:
            return 0
        self.traversal(root, 1, 0, sum_list)
        return sum(sum_list)

# 2. DFS---Stack
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        sum_list = []
        if root is None:
            return 0
        stack = []
        stack.append((root, root.val))
        while stack:
            node, ans = stack.pop()
            if node.right:
                stack.append((node.right, ans * 10 + node.right.val))
            if node.left:
                stack.append((node.left, ans * 10 + node.left.val))
            if not node.right and not node.left:
                sum_list.append(ans)
        return sum(sum_list)


# 3. BFS---Queue
import collections
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        sum_list = []
        if root is None:
            return 0
        queue = collections.deque()
        queue.append((root, root.val))
        while queue:
            node, ans = queue.popleft()
            if node.left:
                queue.append((node.left, ans * 10 + node.left.val))
            if node.right:
                queue.append((node.right, ans * 10 + node.right.val))
            if not node.left and not node.right:
                sum_list.append(ans)

        return sum(sum_list)

