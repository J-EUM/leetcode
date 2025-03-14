# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # p가 왼쪽, q가 오른쪽
        if p.val > q.val:
            p, q = q, p

        while root:
            if p.val <= root.val <= q.val:
                return root
            elif p.val >= root.val:
                root = root.right
            else:
                root = root.left
