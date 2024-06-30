import heapq
from typing import Dict
def solution(s: int, e: int, t: int, edges) -> int:
    ans = -1
    h = []
    heapq.heapify(h)
    # s -> e -> t

    visited = set()
    visited.add(s)
    # [开销, 当前位置, 目的地]
    heapq.heappush(h, (0, s, e, visited))

    while h:
        cost, cur_pos, dis_pos, cur_visited = heapq.heappop(h)
        if cur_pos == e and dis_pos == e:
            # 到达钥匙，去终点
            heapq.heappush(h, (cost, cur_pos, t, cur_visited.copy()))
        elif cur_pos == t and dis_pos == t:
            # 到达终点
            ans = cost
            break
        else:
            for nxt in edges[cur_pos]:
                if nxt not in cur_visited:
                    tmp_visited = cur_visited.copy()
                    tmp_visited.add(nxt)
                    heapq.heappush(h, (cost + edges[cur_pos][nxt], nxt, dis_pos,tmp_visited))
    return ans

def solution2(s: int, e: int, t: int, edges) -> int:
    ans = float("inf")
    visited = set()

    def dfs(cost: int, cur: int, target: int):
        new_target = target
        nonlocal ans
        if cur == t and target == t:
            ans = min(ans, cost)
            return
        if cur == e and target == e:
            new_target = t
        
        for nxt in edges[cur]:
            if nxt not in visited:
                visited.add(nxt)
                dfs(cost + edges[cur][nxt], nxt, new_target)
                visited.remove(nxt)
    visited.add(s)
    dfs(0, s, e)
    return ans



print(solution2(1 - 1, 2 - 1, 3 - 1, {0: {1: 5, 2: 30}, 1: {0: 5}, 2: {0: 30}}))
