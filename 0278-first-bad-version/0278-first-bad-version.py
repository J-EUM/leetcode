# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start < end:
            version_to_check = (start + end) // 2
            if isBadVersion(version_to_check):
                end = version_to_check
            else:
                start = version_to_check + 1
        return start
