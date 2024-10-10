from collections import deque
class Solution:
    def apply(self, generated_map) :
        # write code here
        n, m = len(generated_map), len(generated_map[0])
        visited = set()
        q = deque()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        visited.add((0, 0))
        q.append((0, 0))

        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and generated_map[nx][ny] == 0 and(nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny))
        
        return n * m - len(visited)

print(Solution().apply([[0,1,1,0],[1,0,0,0],[0,1,0,1],[0,1,1,0]]))
