from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            mid = (left + right) // 2
            left_max = helper(left, mid)
            right_max = helper(mid + 1, right)

            # 수정: self.cross_sum()으로 호출
            cross_max = self.cross_sum(nums, left, mid, right)

            return max(left_max, right_max, cross_max)

        return helper(0, len(nums) - 1)

    def cross_sum(self, nums: List[int], left: int, mid: int, right: int) -> int:
        # 왼쪽 최대 부분합 찾기
        left_sum = float('-inf')
        curr_sum = 0
        for i in range(mid, left - 1, -1):
            curr_sum += nums[i]
            left_sum = max(left_sum, curr_sum)

        # 오른쪽 최대 부분합 찾기
        right_sum = float('-inf')
        curr_sum = 0
        for i in range(mid + 1, right + 1):
            curr_sum += nums[i]
            right_sum = max(right_sum, curr_sum)

        return left_sum + right_sum
