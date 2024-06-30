from collections import defaultdict
n, m = map(int, input().split())
valid = set([i for i in range(1, n + 1)])
for _ in range(m):
    u, v, color = input().split()
    if color == "W":
        if int(u) in valid:
            valid.remove(int(u))
        if int(v) in valid:
            valid.remove(int(v))

print(len(valid))
