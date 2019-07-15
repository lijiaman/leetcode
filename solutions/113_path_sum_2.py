def traversal_sum(self, node, target, ans, res_list, final_list):
    if node is not None:
        ans += node.val
        res_list.append(node.val)
    else:
        return

    if ans == target and (not node.left) and (not node.right):
        final_list.append(res_list[:])

    self.traversal_sum(node.left, target, ans, res_list, final_list)
    self.traversal_sum(node.right, target, ans, res_list, final_list)
    res_list.pop()


def pathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    res_list = []
    final_list = []
    self.traversal_sum(root, sum, 0, res_list, final_list)
    return final_list