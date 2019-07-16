# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 0. My initial solution which has unnecessary computation
class Solution:
    def traversal_sum(self, node, ans, target):
        if node is not None:
            ans += node.val
        else:
            return
        if ans == target and (not node.left) and (not node.right):
            self.flag = True
        self.traversal_sum(node.left, ans, target)
        self.traversal_sum(node.right, ans, target)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.flag = False
        if root is None:
            return False
        self.traversal_sum(root, 0, sum)
        return self.flag

# 1. Recursive
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

# 2. DFS---Stack
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, ans = stack.pop()
            if ans == sum and not node.left and not node.right:
                return True
            if node.left:
                stack.append((node.left, node.left.val + ans))
            if node.right:
                stack.append((node.right, node.right.val + ans))

        return False

# 3. BFS---Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        queue = collections.deque([(root, root.val)])
        while queue:
            node, ans = queue.popleft()
            if ans == sum and not node.left and not node.right:
                return True
            if node.left:
                queue.append((node.left, node.left.val + ans))
            if node.right:
                queue.append((node.right, node.right.val + ans))

        return False
