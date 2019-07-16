"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# 1. BFS---Queue
import collections
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i > 0:
                    prev_node.next = node
                prev_node = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root

# 2. BFS, O(1) space
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        prev_level = root
        next_start = root.left
        while prev_level.left:
            prev_level.left.next = prev_level.right
            if prev_level.next:
                prev_level.right.next = prev_level.next.left
                prev_level = prev_level.next
            else:
                prev_level = next_start
                next_start = prev_level.left

        return root
