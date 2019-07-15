def traversal_sum(self, node, ans, target):
    if node is not None:
        ans += node.val
    else:
        return
    if ans == target and (not node.left) and (not node.right):
        self.flag = True
    self.traversal_sum(node.left, ans, target)
    self.traversal_sum(node.right, ans, target)


def hasPathSum(self, root, sum):
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