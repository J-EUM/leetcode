class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)

        k = 2
        for i in range(2, len(nums)):
            if nums[k - 2] != nums[i]:
                nums[k] = nums[i]
                k += 1
        
        return k