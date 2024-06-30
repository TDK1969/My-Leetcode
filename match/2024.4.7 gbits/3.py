from typing import List
from collections import deque

def solution(grid: List[List[int]], m: int, n: int) -> int:
    lowerest_k = -float("inf")
    q = deque()
    q.append((0, 0, grid[0][0], grid[0][0]))
    while q:
        x, y, cur_k, low_k = q.popleft()
        if x == m - 1 and y == n - 1:
            # 到达终点,取最小值的最大值
            if low_k < 0:
                lowerest_k = max(lowerest_k, low_k)
        else:
            # 向右走
            if y != n - 1:
                q.append((x, y + 1, cur_k + grid[x][y + 1], min(low_k, cur_k + grid[x][y + 1])))
            if x != m - 1:
                q.append((x + 1, y, cur_k + grid[x + 1][y], min(low_k, cur_k + grid[x + 1][y])))

    if lowerest_k == -float("inf"):
        return 0
    return -lowerest_k + 1

print(solution([[1, 1, 3], [5, 10, 1]], 2, 3))