from typing import *
from collections import deque
def solution(n: int, m: int, l: List[int]) -> int:
    mod = (10 ** 9) + 7
    # love[u] = v表示u暗恋v
    love = [-1] * n
    # degree表示入度
    degree = [0] * n
    for u, v in l:
        love[u - 1] = v - 1
        degree[v - 1] += 1
    zero_degree = []
    ans = 0
    q = deque()

    for i in range(n):
        if degree[i] == 0:
            q.append(i)
            zero_degree.append(i)

    while q:
        ans = (ans + len(q) * (len(q) + 1) // 2) % mod
        t = q.popleft()
        degree[love[t]] -= 1
        if degree[love[t]] == 0:
            q.append(love[t])
    
    return ans


print(solution(5, 1, [[1, 2], [2, 3], [3, 5], [4, 5]]))
    


