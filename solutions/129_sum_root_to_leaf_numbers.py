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


def sumNumbers(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    sum_list = []
    if root is None:
        return 0
    self.traversal(root, 1, 0, sum_list)
    return sum(sum_list)