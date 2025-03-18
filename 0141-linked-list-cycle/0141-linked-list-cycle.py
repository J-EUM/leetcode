# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        linked_list = []
        cur = head
        while cur:
            if cur in linked_list:
                return True
            linked_list.append(cur)
            cur = cur.next
        return False
      