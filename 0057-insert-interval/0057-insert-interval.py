from collections import deque


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        q = deque(intervals)
        temp = newInterval

        while q:
            interval = q.popleft()
            if interval[1] < temp[0]:
                result.append(interval)
            elif interval[0] > temp[1]:
                result.append(temp)
                temp = interval
            else:
                temp = [min(interval[0], temp[0]), max(interval[1], temp[1])]

        result.append(temp)
        return result
