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

# 2. BFS---O(1) space
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        node = root
        next_level = dummy = Node(0, None, None, None)
        while node:
            next_level.next = node.left
            if next_level.next:
                next_level = next_level.next
            next_level.next = node.right
            if next_level.next:
                next_level = next_level.next
            node = node.next
            if not node:
                next_level = dummy
                node = dummy.next

        return root


