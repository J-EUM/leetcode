class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1, 0, -1):
            if nums.count(nums[i]) > 2:
                nums.pop(i)

        return len(nums)