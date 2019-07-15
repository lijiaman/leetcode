
## I. Recursion
def check_mirror(self, node_1, node_2):
    if node_1 is None and node_2 is None:
        return True
    if node_1 is None or node_2 is None:
        return False

    if node_1.val == node_2.val:
        return self.check_mirror(node_1.left, node_2.right) and self.check_mirror(node_1.right, node_2.left)
    else:
        return False


def isSymmetric(self, root: TreeNode) -> bool:
    if root is None:
        return True

    return self.check_mirror(root.left, root.right)


### II. Use Queue

def isSymmetric(self, root: TreeNode) -> bool:
    if root is None:
        return True

    queue = [[root.left, root.right]]
    while len(queue) > 0:
        pair = queue.pop(0)
        left_node = pair[0]
        right_node = pair[1]
        if left_node is None and right_node is None:
            continue
        if left_node is None or right_node is None:
            return False
        if left_node.val == right_node.val:
            queue.append([left_node.left, right_node.right])
            queue.append([left_node.right, right_node.left])
        else:
            return False

    return True