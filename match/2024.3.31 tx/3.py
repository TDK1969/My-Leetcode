from typing import List
from collections import deque

def solution(n: int, edges: List[List[int]]) -> int:
    # 找强连通分量
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    group = []
    in_group = [-1 for _ in range(n)]

    for i in range(n):
        if in_group[i] == -1:
            if len(group) == 2:
                return 0
            group.append([i])
            in_group[i] = len(group) - 1
            q = deque()
            q.append(i)

            while q:
                t = q.popleft()
                for nxt in graph[t]:
                    if in_group[nxt] == -1:
                        group[-1].append(nxt)
                        in_group[nxt] = len(group) - 1
                        q.append(nxt)
    
    if len(group) > 2:
        return 0
    else:
        return len(group[0]) * len(group[1])

print(solution(4, [[1, 2]]))

        