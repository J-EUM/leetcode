from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        result = [[-1] * n for _ in range(m)]

        q = deque([])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    q.append((i, j, 0))

        while q:
            x, y, distance = q.popleft()

            dx = (-1, 1, 0, 0)
            dy = (0, 0, -1, 1)

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < m and ny >= 0 and ny < n and result[nx][ny] == -1:
                    result[nx][ny] = distance + 1
                    q.append((nx, ny, distance + 1))
        
        return result
