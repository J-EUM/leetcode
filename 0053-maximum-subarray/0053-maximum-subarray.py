class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_temp = -10 ** 4
        temp = -10 ** 4
        left = 0
        for i in range(len(nums)):
            if nums[i] > temp + nums[i]:
                temp = nums[i]
                left = i
            else:
                temp += nums[i]
            max_temp = max(max_temp, temp)
        
        temp = -10 ** 4
        right = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > temp + nums[i]:
                temp = nums[i]
                right = i
            else:
                temp += nums[i]
            max_temp = max(max_temp, temp)

        return max_temp
