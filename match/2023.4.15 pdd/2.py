from typing import List

def solution(a: List[int]) -> int:
    MOD = 10 ** 7 + 7
    ans = 0
    cnt = a[0]
    l = 1
    for i in range(1, len(a)):
        if a[i] != a[i - 1]:
            ans = (ans + (a[i] * l) % MOD + cnt) % MOD
            l += 1
            cnt = (cnt + a[i] * l) % MOD
        else:
            l = 1
            cnt = a[i]
    
    return ans

print(solution([1]))

