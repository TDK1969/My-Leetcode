from typing import List

def mat_mul(mat_1: List[List[int]], mat_2: List[List[int]], mod: int):
    n = len(mat_1)
    mat = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mat[i][j] = (mat[i][j] + mat_1[i][k] * mat_2[k][j]) % mod
    return mat
                
def mat_mul2(mat_1: List[List[int]], mat_2: List[int], mod: int):
    n = len(mat_1)
    mat = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i] = (mat[i] + mat_1[i][j] * mat_2[j]) % mod
    return mat

def solution(n: int, k: int) -> int:
    mod = 998244353
    if n <= k:
        return 2 ** (n - 1)
    else:
        mat = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(k):
            mat[0][i] = 1
        for i in range(1, k):
            mat[i][i - 1] = 1
        
        ori = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(k):
            ori[i][i] = 1


        ans2 = []
        for i in range(k):
            ans2.append(2 ** (k - i - 1))
        
        t = n - k
        while t:
            if (t & 1):
                ori = mat_mul(ori, mat, mod)
            mat = mat_mul(mat, mat, mod)
            t = t >> 1
        
        ans2 = mat_mul2(ori, ans2, mod)
        return ans2[0]
print(solution(10, 8))
        


