# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1.1 BFS---Queue
# 40ms(61.68%), 13.1M(80.53%)
import collections
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        res_list = []
        while queue:
            size = len(queue)
            for i in range(size):
                curr_node = queue.popleft()
                if i == size-1:
                    res_list.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return res_list

# 1.2 BFS---Queue
# 36ms(96.04%), 13.2M(61.79%)
import collections
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        queue = collections.deque()
        queue.append((root, 0))
        res_list = []
        level_dict = {}
        while queue:
            node, level = queue.popleft()
            if level not in level_dict:
                level_dict[level] = 1
                res_list.append(node.val)
            if node.right:
                queue.append((node.right, level + 1))
            if node.left:
                queue.append((node.left, level + 1))
        return res_list

# 2. DFS Recursively
# 36ms(84.48%), 13.2M(50.07%)
class Solution(object):
    def dfs(self, node, level, level_dict, res_list):
        if level not in level_dict:
            res_list.append(node.val)
            level_dict[level] = 1
        if node.right:
            self.dfs(node.right, level + 1, level_dict, res_list)
        if node.left:
            self.dfs(node.left, level + 1, level_dict, res_list)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        level_dict = {}
        res_list = []
        self.dfs(root, 0, level_dict, res_list)
        return res_list

# 3. DFS Iteratively---Stack
# 32ms(96.04%), 13.1M(79.21%)
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [(root, 0)]
        level_dict = {}
        res_list = []
        while stack:
            node, level = stack.pop()
            if level not in level_dict:
                level_dict[level] = 1
                res_list.append(node.val)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))

        return res_list
