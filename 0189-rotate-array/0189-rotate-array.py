class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import deque
        q = deque(nums)
        for i in range(-k, 0):
            q.appendleft(q.pop())
        nums[:] = list(q)
        