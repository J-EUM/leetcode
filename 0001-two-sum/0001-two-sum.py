class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in checked:
                return [i, checked[value]]
            checked[nums[i]] = i
