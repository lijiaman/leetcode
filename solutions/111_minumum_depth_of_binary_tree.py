def traversal_path(self, depth, node):
    if (not node.left) and (not node.right):
        if depth < self.min_path:
            self.min_path = depth
        return
    if node.left:
        self.traversal_path(depth + 1, node.left)
    if node.right:
        self.traversal_path(depth + 1, node.right)


def minDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.min_path = float('inf')
    if root is None:
        return 0
    self.traversal_path(1, root)
    return self.min_path