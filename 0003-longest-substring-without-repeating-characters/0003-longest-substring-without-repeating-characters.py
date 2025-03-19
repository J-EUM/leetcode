class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1
        answer = 0

        while right <= len(s):
            sub = s[left:right]
            if len(sub) == len(set(sub)):
                answer = max(answer, right - left)
                right += 1
            else:
                left += 1

        return answer
