from typing import List

# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))

def solution(n: int, m: int, a: List[int], b: List[int], c: List[int]) -> int:
    d = dict()
    ans = sum(c)

    for i in range(n):
        tag = a[i]
        if b[i] > c[i]:
            # 打标签是有用的
            if tag not in d:
                d[tag] = i
                ans += b[i] - c[i]
            elif tag in d and b[i] - c[i] > b[d[tag]] - c[d[tag]]:
                ans += c[d[tag]] - b[d[tag]] + b[i] - c[i]
                d[tag] = i
    
    return ans

print(solution(3, 3, [1,2,1], [5,4,3], [-1, 2, -100]))
