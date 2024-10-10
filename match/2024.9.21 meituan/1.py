def solution(n: int) -> int:
    if n <= 2:
        return n
    ans = 2
    cur = 2

    while cur < n:
        cur += cur - 1
        ans += 1
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    print(solution(n))

