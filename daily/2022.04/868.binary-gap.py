"""
日期: 2022-04-24
题目: 二进制间距
链接: https://leetcode-cn.com/problems/binary-gap/
"""
class Solution:
    def binaryGap(self, n: int) -> int:
        bit = 1
        one_bit = []
        i = 0
        while n >= bit:
            if n & bit == bit:
                one_bit.append(i)
            i += 1
            bit = bit << 1
        
        if len(one_bit) < 2:
            return 0
        else:
            return max([one_bit[i] - one_bit[i - 1] for i in range(1, len(one_bit))])

test = Solution()
print(test.binaryGap(22))

