# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. O(n) space for storing sorted array
# 96ms(33.75%), 19.7M(78.33%)
import collections
class BSTIterator:

    def __init__(self, root: TreeNode):
        stack = collections.deque()
        self.res_queue = collections.deque()
        while True:
            while root:
                stack.append(root)
                root = root.left
            if len(stack) == 0:
                break
            node = stack.pop()
            if node:
                self.res_queue.append(node.val)
                root = node.right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if len(self.res_queue) > 0:
            return self.res_queue.popleft()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.res_queue) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# 2. O(h) space for maintaining a stack
# 88ms(81.21%), 20.1M(42.67%)
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.dump_leftmost(root)

    def dump_leftmost(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if len(self.stack) > 0:
            curr_node = self.stack.pop()
            self.dump_leftmost(curr_node.right)
            return curr_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()