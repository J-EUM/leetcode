class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_temp = -10 ** 4
        temp = -10 ** 4
        for i in range(len(nums)):
            if nums[i] > temp + nums[i]:
                temp = nums[i]
            else:
                temp += nums[i]
            max_temp = max(max_temp, temp)

        return max_temp
