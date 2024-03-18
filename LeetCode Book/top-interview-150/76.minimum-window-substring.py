"""
日期: 2022-07-14
题目: 最小覆盖子串
链接: https://leetcode-cn.com/problems/minimum-window-substring/
"""

from typing import *
from collections import *
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        # 滑动窗口,当不包含t时向右扩展,当包含t时向左移动
        t_counter = defaultdict(int)
        for alpha in t:
            t_counter[alpha] += 1
        window_counter = defaultdict(int)
        n = len(s)
        i = j = 0
        ans = s
        # flag用于判断是否不存在包含的子字符串
        flag = False

        # 判断是否包含
        def check():
            for alpha in t_counter:
                if t_counter[alpha] > window_counter[alpha]:
                    return False
            return True
        
        while j <= n:
            # 如果s[i:j]包含,则窗口左沿右移
            if i < j and check():
                if j - i <= len(ans):
                    ans = s[i : j]
                    flag = True
                window_counter[s[i]] -= 1
                i += 1
            # 不包含则右移
            else:
                if j == n:
                    break
                window_counter[s[j]] += 1
                j += 1
        
        return ans if flag else ""
    
    def minWindow(self, s: str, t: str) -> str:
        # 滑动窗口,时间复杂度不需要考虑字符集大小,即不需要check()函数
        # s的长度必须不小于t
        if len(s) < len(t): return ''
        #初始化
        rec = defaultdict(int)
        # len_t表示窗口中的缺少的t中的字符个数
        len_t = len(t)
        minLeft, minRight = 0, len(s)

        # 记录t中各个字母的出现频次
        for i in t:
            rec[i] += 1

        #开始寻找子串
        left = 0
        for right, str in enumerate(s):
            if rec[str] > 0:  #找到t中的字母,对于不存在的valu而等于0（这就是defaultdic的方便之处）
                len_t -= 1
            # rec中值为负的,要么是不在t中的字符,要么是在t中但是多出来的字符
            rec[str] -= 1 #值为负的要么是多余的在t中的字符，要么是不在t中的字母，便于后面left移动

            if len_t == 0:
                while rec[s[left]] < 0: #值为负的要么是多余的在t中的字符，要么是不在t中的字母，left向右移动
                    rec[s[left]] += 1
                    left += 1

                if right - left < (minRight - minLeft):  #上一步left到位，现在更新最小区间
                    minLeft, minRight = left, right

                # 此时[left, right]已经是一个最小窗口,因此窗口拓展没有意义,因此缩小,破坏窗口
                rec[s[left]] += 1 # 开始找下一个窗口
                left += 1
                len_t += 1

        return '' if minRight == len(s) else s[minLeft:minRight+1]

test = Solution()
print(test.minWindow("aaabc", "aab"))



