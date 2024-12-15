class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nxt = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[nxt], nums[i] = nums[i], nums[nxt]
                nxt += 1
        return nxt
        