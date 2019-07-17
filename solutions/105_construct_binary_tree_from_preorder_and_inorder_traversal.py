# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def construct(self, preorder, inorder):
        if len(preorder) > 0:
            root = TreeNode(preorder[0])
            root_idx = inorder.index(root.val)
            root.left = self.construct(preorder[1:1 + root_idx], inorder[:root_idx])
            root.right = self.construct(preorder[1 + root_idx:], inorder[root_idx + 1:])

            return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.construct(preorder, inorder)
