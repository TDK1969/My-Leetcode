class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        # 或调库pow
        def quickmi(x: int, y: int) -> int:
            ret, mi = 1, x
            while y > 0:
                if y % 2 == 1:
                    ret = ret * mi % mod
                mi = mi * mi % mod
                y //= 2
            return ret

        return quickmi(5, (n + 1) // 2) * quickmi(4, n // 2) % mod




