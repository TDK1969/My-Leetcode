class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def quick_algorithm(a, b, c):
            # return a ^ b mod c
            a = a % c
            ans = 1
            while b != 0:
                if b & 1:
                    ans = (ans * a) % c
                b >>= 1
                a = (a * a) % c
            return ans

        pMax = quick_algorithm(power, k - 1, modulo)


        for i in range(len(s) - k)
        for i in range(len(s) - k + 1):
            if calHash(s[i:i + k], power, modulo) == hashValue:
                return s[i:i + k]

test = Solution()
print(test.subStrHash(s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0))

