
def check(s: str) -> bool:
    n = len(s)
    if n == 1:
        return True
    if s in (s + s)[1:-1]:
        return True
    return False
    # for i in range(2, n):
    #     if (n % i == 0):
    #         c = {}
    #         for k in range(n // i):
    #             sub = s[k * i:(k + 1) * i]
    #             if sub not in c:
    #                 c[sub] = 0
    #             c[sub] += 1
    #         if len(c) > 3:
    #             return False

    #         # 只有两种子串a和b，且a出现1次，b出现多次
    #         if len(c) == 2:
    #             a, b = c.keys()
    #             if c[b] == 1 and c[a] > 1:
    #                 a, b = b, a
                
    #             if c[b] > 1:
    #                 # 以b为基准



print(check("abcabc"))
