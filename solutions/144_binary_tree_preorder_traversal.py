# 1. Recursive Preorder Traversal
class Solution:
    def visit(self, node, n_list):
        if node is None:
            return
        n_list.append(node.val)
        self.visit(node.left, n_list)
        self.visit(node.right, n_list)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        n_list = []
        self.visit(root, n_list)
        return n_list

# 2. Iterative Preorder Traversal---Stack
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        n_list = []
        stack = [root]
        while stack:
            node = stack.pop()
            n_list.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return n_list