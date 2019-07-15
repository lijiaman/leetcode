"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        queue = [root]
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if i > 0:
                    prev_node.next = node
                prev_node = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
