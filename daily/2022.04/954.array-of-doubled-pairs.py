"""
日期: 2022-04-01
题目: 二倍数对数组
链接: https://leetcode-cn.com/problems/array-of-doubled-pairs/
"""
from typing import List
from collections import Counter

from sortedcontainers import SortedSet
from operator import neg
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        p = []
        n = []
        z = 0
        for num in arr:
            if num > 0:
                p.append(num)
            if num < 0:
                n.append(num)
            if num == 0:
                z += 1
        
        #对0的数目进行判断，必须为偶数
        if z & 1 == 1:
            return False
        
        p = SortedSet(p)
        n = SortedSet(n, neg)

        for pnum in p:
            if counter[pnum] < 0:
                return False
            else:
                for _ in range(counter[pnum]):
                    if counter[2 * pnum] == 0:
                        return False
                    else:
                        counter[pnum] -= 1
                        counter[2 * pnum] -= 1
        
        for nnum in n:
            if counter[nnum] < 0:
                return False
            else:
                for _ in range(counter[nnum]):
                    if counter[2 * nnum] == 0:
                        return False
                    else:
                        counter[nnum] -= 1
                        counter[2 * nnum] -= 1
        return True

test = Solution()
print(test.canReorderDoubled([-2,-4]))


