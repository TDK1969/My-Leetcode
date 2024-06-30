from typing import List
from collections import deque

def solution(n: int, m: int, input_s: List[str]) -> int:
    ans = 0
    target = "tencent"
    grid = [["" for _ in range(m)] for _ in range(n)]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    t1 = dict()
    e2 = dict()
    n3 = dict()
    c4 = dict()
    e5 = dict()
    n6 = dict()
    t7 = dict()
    for i in range(n):
        for j, alpha in enumerate(input_s[i]):
            grid[i][j] = alpha
            if alpha == "t":
                t1[(i, j)] = 0
                t7[(i, j)] = 0
            elif alpha == "e":
                e2[(i, j)] = 0
                e5[(i, j)] = 0
            elif alpha == "n":
                n3[(i, j)] = 0
                n6[(i, j)] = 0
            elif alpha == "c":
                c4[(i, j)] = 0
    
    for x, y in n6.keys():
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "t":
                n6[(x, y)] += 1
    
    for x, y in e5.keys():
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "n":
                e5[(x, y)] += n6[(nx, ny)]
    
    for x, y in c4.keys():
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "e":
                c4[(x, y)] += e5[(nx, ny)]
    
    for x, y in n3.keys():
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "c":
                n3[(x, y)] += c4[(nx, ny)]
    
    for x, y in e2.keys():
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "n":
                e2[(x, y)] += n3[(nx, ny)]
    
    for x, y in t1.keys():
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "e":
                t1[(x, y)] += e2[(nx, ny)]
    
    for key in t1:
        ans += t1[key]

    return ans


print(solution(3, 3, ["ten", "nec", "ten"]))




