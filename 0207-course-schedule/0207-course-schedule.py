from collections import deque
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        for u in range(numCourses):
            for v in graph[u]:
                indegree[v] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return count == numCourses
