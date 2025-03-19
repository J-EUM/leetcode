class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_set = set()
        answer = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            answer = max(answer, right + 1 - left)

        return answer

        # left, right = 0, 1
        # answer = 0

        # while right <= len(s):
        #     sub = s[left:right]
        #     if len(sub) == len(set(sub)):
        #         answer = max(answer, right - left)
        #         right += 1
        #     else:
        #         left += 1

        # return answer
