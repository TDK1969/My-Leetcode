N, M = 2, 1
dislikes = []
for _ in range(M):
    X, Y = 1, 1
    dislikes.append((X, Y))

girls = [0 for _ in range(N)]
boys = list(range(1, N + 1))
visited = [False for _ in range(N)]

def dfs(current):
    if current == N:
        unhappy = 0
        for i in range(N):
            pre, nxt = girls[(i - 1) % N], girls[i]
            if (i + 1, pre) in dislikes or (i + 1, nxt) in dislikes:
                unhappy += 1
        return unhappy
    min_unhappy = float("inf")
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            girls[current] = boys[i]
            min_unhappy = min(min_unhappy, dfs(current + 1))
            visited[i] = False
    return min_unhappy

print(dfs(0))
           