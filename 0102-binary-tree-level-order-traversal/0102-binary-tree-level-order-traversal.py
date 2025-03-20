# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_map = {}

        def build_level_map(node, level):
            if node:
                if level not in level_map:
                    level_map[level] = []
                level_map[level].append(node.val)
                build_level_map(node.left, level + 1)
                build_level_map(node.right, level + 1)
            
        build_level_map(root, 0)

        return [v for _, v in level_map.items()]
