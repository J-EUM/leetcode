from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        og_color = image[sr][sc]
        if color == og_color:
            return image

        q = deque([(sr, sc)])
        dc = (0, 0, -1, 1)
        dr = (-1, 1, 0, 0)

        while q:
            r, c = q.pop()
            image[r][c] = color

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr >= 0 and nr < len(image) and nc >= 0 and nc < len(image[0]):
                    if image[nr][nc] == og_color and (nr, nc) not in q:
                        q.append((nr, nc))

        return image
        