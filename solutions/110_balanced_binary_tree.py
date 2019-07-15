def check(self, node):
    if node is None:
        return -1

    left_h = self.check(node.left)
    right_h = self.check(node.right)
    if abs(left_h - right_h) > 1:
        self.flag = False

    return max(left_h, right_h) + 1


def isBalanced(self, root: TreeNode) -> bool:
    self.flag = True
    if root is None:
        return True
    self.check(root)
    return self.flag