# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 0. My Initial Recursive version
class Solution:
    def traversal_sum(self, node, target, ans, res_list, final_list):
        if not node:
            return
        ans += node.val
        res_list.append(node.val)
        if ans == target and (not node.left) and (not node.right):
            final_list.append(res_list[:])
        self.traversal_sum(node.left, target, ans, res_list, final_list)
        self.traversal_sum(node.right, target, ans, res_list, final_list)
        res_list.pop()

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res_list = []
        final_list = []
        self.traversal_sum(root, sum, 0, res_list, final_list)
        return final_list

# 1. Recursive
class Solution:
    def dfs(self, node, target, ans, res_list, final_list):
        if not node:
            return
        if not node.left and not node.right and node.val + ans == target:
            final_list.append(res_list[:] + [node.val])
            return
        self.dfs(node.left, target, ans + node.val, res_list + [node.val], final_list)
        self.dfs(node.right, target, ans + node.val, res_list + [node.val], final_list)

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        final_list = []
        self.dfs(root, sum, 0, [], final_list)
        return final_list


# 2. DFS---Stack
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res_list = []
        stack = [(root, [root.val], root.val)]
        while stack:
            node, val_list, ans = stack.pop()
            if not node.left and not node.right and ans == sum:
                res_list.append(val_list[:])
            if node.left:
                stack.append((node.left, val_list + [node.left.val], ans + node.left.val))
            if node.right:
                stack.append((node.right, val_list + [node.right.val], ans + node.right.val))

        return res_list

# 3. BFS---Queue
import collections
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res_list = []
        queue = collections.deque([(root, [root.val], root.val)])
        while queue:
            node, val_list, ans = queue.popleft()
            if not node.left and not node.right and ans == sum:
                res_list.append(val_list[:])
            if node.left:
                queue.append((node.left, val_list + [node.left.val], ans + node.left.val))
            if node.right:
                queue.append((node.right, val_list + [node.right.val], ans + node.right.val))

        return res_list