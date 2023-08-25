from typing import List
n = int(input())
lengths = list(map(int, input().strip().split()))

def func(n: int, lengths: List) -> int:
    lengths.sort()
    ans = 0
    for i in range(0, n):
        temp = min(n - i, lengths[i])
        ans = max(ans, temp)
    return ans

print(func(n, lengths))