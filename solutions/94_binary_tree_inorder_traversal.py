## I. Recursion
def visit(self, node, n_list):
    if node is None:
        return
    self.visit(node.left, n_list)
    n_list.append(node.val)
    self.visit(node.right, n_list)


def inorderTraversal(self, root: TreeNode) -> List[int]:
    n_list = []
    self.visit(root, n_list)
    return n_list

## II. Iteratively
def inorderTraversal(self, root: TreeNode) -> List[int]:
    res_list = []
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if len(stack) == 0:
            break
        node = stack.pop()
        res_list.append(node.val)
        root = node.right

    return res_list