# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if min(p.val, q.val) > root.val:
                root = root.right
            elif max(p.val, q.val) < root.val:
                root = root.left
            else:
                return root      
  