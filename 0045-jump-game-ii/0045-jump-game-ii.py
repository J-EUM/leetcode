class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        for i in range(len(nums)):
            nums[i] += i
        
        step = 1
        i, max_i = 0, nums[0]

        while i <= max_i:
            if max_i >= len(nums) - 1:
                return step

            i, max_i =max_i + 1, max(max_i, max(nums[i:max_i + 1]))

            step += 1
