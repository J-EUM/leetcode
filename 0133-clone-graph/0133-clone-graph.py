from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return copy.deepcopy(node)
        # nodes = {}
        # q = deque([node])

        # while q:
        #     cur = q.popleft()
        #     if cur:
        #         nodes[cur.val] = None
        #         for n in cur.neighbors:
        #             if not nodes[cur.val]:
        #                 nodes[cur.val] = []
        #             nodes[cur.val].append(n.val)
        #             if n not in q and n.val not in nodes:
        #                 q.append(n)
        
        # nodes_list = [None]
        # for i in range(1, len(nodes)+1):
        #     nodes_list.append(Node(i))

        # for i in range(1, len(nodes)+1):
        #     if nodes[i]:
        #         for n_val in nodes[i]:  # 이웃 val만 있는 리스트
        #             if not nodes_list[i].neighbors:
        #                 nodes_list[i].neighbors = []
        #             nodes_list[i].neighbors.append(nodes_list[n_val])

        # return nodes_list[-1]
