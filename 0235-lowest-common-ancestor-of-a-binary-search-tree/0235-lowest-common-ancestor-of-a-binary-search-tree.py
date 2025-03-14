from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tree = {}
        p_index = 0
        q_index = 0
        
        queue = deque([(root, 1)])
        while p_index == 0 or q_index == 0:
            node, index = queue.popleft()
            tree[index] = node
            if node.val == p.val:
                p_index = index
            if node.val == q.val:
                q_index = index

            if node.left:
                queue.append((node.left, index * 2))
            if node.right:
                queue.append((node.right, index * 2 + 1))
        
        while p_index != q_index:
            print(p_index, q_index)
            if p_index > q_index:
                p_index //= 2
            else:
                q_index //=2
    
        return tree[p_index]
