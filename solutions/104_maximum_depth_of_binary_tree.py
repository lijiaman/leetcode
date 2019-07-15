def maxDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    queue = [root]
    level_cnt = 0
    while len(queue) > 0:
        level_cnt += 1
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)