def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    if root is None:
        return []
    res_list = []
    queue = [root]
    order_flag = True
    while len(queue) > 0:
        curr_level = []
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            curr_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not order_flag:
            curr_level.reverse()
        res_list.append(curr_level)

        order_flag = (not order_flag)

    return res_list