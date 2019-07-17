# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def construct(self, inorder, postorder):
        if len(postorder) > 0:
            root = TreeNode(postorder[-1])
            root_idx = inorder.index(root.val)
            root.left = self.construct(inorder[:root_idx], postorder[:root_idx])
            root.right = self.construct(inorder[root_idx + 1:], postorder[root_idx:-1])

            return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.construct(inorder, postorder)