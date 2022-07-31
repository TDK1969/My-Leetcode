
from typing import *
def test(n: int, k: int, t: List[List[int]]) -> int:
    basic = sum(i[0] for i in t)
    dp = [0 for _ in range(k + 1)]
    
    for i in range(n):
        for j in range(k, -1, -1):
            if j >= t[i][2]:
                dp[j] = max(dp[j], dp[j - t[i][2]] + t[i][1] - t[i][0])
            else:
                break

    
    return 1500 + dp[-1] + basic
    
print(test(3, 5, [[1, 4, 2], [1, 2, 1], [1, 3, 3]]))
