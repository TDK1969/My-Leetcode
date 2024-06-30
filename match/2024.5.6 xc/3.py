n, q = map(int, input().split())
nums = list(map(int, input().split()))
mod = 6
def pow(a: int, b: int, mod: int):
    res = 1
    while b:
        if b & 1:
            res = (res * a) % mod
        a = (a * a) % mod
        b >>= 1
    return res

def getInv(x: int, mod: int):
    return pow(x, mod - 2, mod)

pre = [1]
for num in nums:
    pre.append(pre[-1] * num)
print(pre)

for _ in range(q):
    l, r = map(int, input().split())
    print(pre[r] * getInv(pre[l - 1], mod) % mod)
