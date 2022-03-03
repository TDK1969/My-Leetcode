class Solution:
    def addDigits(self, num: int) -> int:
        def bitSum(num: int):
            ans = 0
            while num:
                ans += num % 10
                num = num // 10
            return ans
        while num >= 10:
            num = bitSum(num)
        return num
