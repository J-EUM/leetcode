from collections import deque
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses  # 0: 미방문, 1: 방문중, 2: 방문완료
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(node):  # 사이클이 있는지
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return False

            visited[node] = 1
            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True
            visited[node] = 2
            return False

        for i in range(numCourses):
            if visited[i] == 0:
                if dfs(i):
                    return False
        return True
