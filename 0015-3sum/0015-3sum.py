class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for i in range(len(nums) - 2):
            num1 = nums[i]
            complement = 0 - num1

            left = i + 1
            right = len(nums) - 1
            while left < right:
                num_left, num_right = nums[left], nums[right]
                if num_left + num_right > complement:
                    right -= 1
                elif num_left + num_right == complement:
                    result.add((num1, num_left, num_right))
                    left += 1
                    right -= 1
                else:
                    left += 1

        return list(map(list, result))
