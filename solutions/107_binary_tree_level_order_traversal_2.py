# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res_list = []
        queue = [root]
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
            res_list.append(curr_level)

        res_list.reverse()
        return res_list
