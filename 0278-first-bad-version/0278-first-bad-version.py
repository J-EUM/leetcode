# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        bad_version = n
        start = 1
        end = n
        while start <= end:
            version_to_check = (start + end) // 2
            if isBadVersion(version_to_check):
                bad_version = min(bad_version, version_to_check)
                end = version_to_check - 1
            else:
                start = version_to_check + 1
        return bad_version
      