n, m = list(map(int, input().split()))
scores = [[0 for _ in range(n)] for _ in range(m)]
for i in range(n):
    s = input().lower()
    for k in range(m):
        scores[k][i] = ord(s[k]) - ord("a") + 1

from math import ceil
ans = []
for i in range(m):
    ans.append([ceil(sum(sorted(scores[i])[1:-1]) / (n - 2)), i + 1])
print(ans)