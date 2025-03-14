class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        temp = newInterval

        for interval in intervals:
            if interval[1] < temp[0]:
                result.append(interval)
            elif interval[0] > temp[1]:
                result.append(temp)
                temp = interval
            else:
                temp = [min(interval[0], temp[0]), max(interval[1], temp[1])]

        result.append(temp)
        return result
