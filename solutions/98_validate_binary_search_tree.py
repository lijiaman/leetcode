
## I. Recursion
def check_order(self, node, lower=-float('inf'), upper=float('inf')):
    if node is None:
        return True
    if node.val <= lower or node.val >= upper:
        return False
    return self.check_order(node.left, lower, min(node.val, upper)) and self.check_order(node.right,
                                                                                         max(lower, node.val), upper)


def isValidBST(self, root: TreeNode) -> bool:
    return self.check_order(root)

## II. Iteratively
def isValidBST(self, root: TreeNode) -> bool:
    if root is None:
        return True
    stack = [[root, -float('inf'), float('inf')]]
    while len(stack) > 0:
        node, lower, upper = stack.pop()
        if node is None:
            continue
        if node.val <= lower or node.val >= upper:
            return False
        stack.append([node.left, lower, min(upper, node.val)])
        stack.append([node.right, max(lower, node.val), upper])

    return True

## III. In-order Traversal

