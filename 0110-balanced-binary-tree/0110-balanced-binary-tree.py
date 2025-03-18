# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth = {}

        def get_depth(idx, node):
            if node:
                left_depth, left_balanced = get_depth(idx * 2, node.left)
                right_depth, right_balanced = get_depth(idx * 2 + 1, node.right)

                balanced = left_balanced and right_balanced and abs(left_depth - right_depth) <= 1
                depth[idx] = max(left_depth, right_depth) + 1
                return depth[idx], balanced
            else:
                return 0, True

        _, answer = get_depth(1, root)

        return answer
