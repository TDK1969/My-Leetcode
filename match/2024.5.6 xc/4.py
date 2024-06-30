n = 3
values = [1, 2, 3]
edges = {0: [1], 1: [0, 2], 2: [1]}


def find_paths(start: int) -> int:
    res = 0
    def dfs(cur: int, pre: int, s: int):
        nonlocal res
        if s % 3 == 0:
            res += 1
        for nxt in edges[cur]:
            if nxt != pre:
                dfs(nxt, cur, s + values[nxt])
    dfs(start, -1, values[start])
    return res

for i in range(n):
    print(find_paths(i))