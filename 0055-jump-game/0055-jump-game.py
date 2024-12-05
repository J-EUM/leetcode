class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 2 3 1 1 4
        # 2 4 3 4  

        # 3 2 1 0 4
        # 3 3 3 3 

        # 3 2 1 0 1 1
        # 3 3 3 3 

        max_i = nums[0]
        i = 0
        while i <= max_i:
            max_i = max(max_i, nums[i] + i)
            if nums[i] + i >= len(nums) - 1:
                return True
            i += 1
        return False
        