from typing import *
from collections import defaultdict
from math import gcd

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def solution(n: int, s: int, e: int, edges: List[List[int]]) -> str:
    path = defaultdict(dict)
    for x, y, w in edges:
        path[x][y] = w
        path[y][x] = w
    flag = False
    res = [float("inf"), 1]
    visited = set()
    def dfs(cur: int, minEnergy: int, maxEnergy: int):
        if cur == e:
            nonlocal flag
            flag = True
            # 找到终点，更新最小比值
            if (res[0] / res[1]) > (maxEnergy / minEnergy):
                res[0], res[1] = maxEnergy, minEnergy
            return
        # 未找到终点，继续寻找
        for nxt in path[cur]:
            if nxt not in visited:
                visited.add(nxt)
                dfs(nxt, min(minEnergy, path[cur][nxt]), max(maxEnergy, path[cur][nxt]))
                visited.remove(nxt)
    visited.add(1)
    dfs(s, float("inf"), -float("inf"))
    if flag:
        temp = gcd(res[0], res[1])
        res[0], res[1] = res[0] // temp, res[1] // temp
        if res[1] == 1:
            return f"{res[0]}"
        else:
            return f"{res[0]}/{res[1]}"
    else:
        return "%%%"


print(solution(10, 3, 10, [[1, 2, 2], [1,3,6],[1,6,3],[2,7,5],[2,6,1],[2,5,3],[3,6,5],[3,7,7],[5,6,6],[6,9,9],[7,9,11],[9,10,13]]))