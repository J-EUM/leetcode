class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ordered_list = []
        for x, y in points:
            d = ((x ** 2) + (y ** 2)) ** (1/2)
            ordered_list.append((x, y, d))
            
        ordered_list.sort(key=lambda x:x[2])

        result = []
        for i in range(k):
            x, y, _ = ordered_list[i]
            result.append([x, y])

        return result
