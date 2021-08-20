class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        l = 0
        while l < n:
            r = l + 2 * k - 1
            mid = l + k - 1
            if mid >= n:
                mid = n - 1
            while l < mid:
                s[l] ,s[mid] = s[mid], s[l]
                l += 1
                mid -= 1
            l = r + 1
        return "".join(s)

class Solution2:
    def reverseStr(self, s: str, k: int) -> str:
        left, mid, right = 0, k, 2 * k                  # 初始化左中右指针
        res = ''                                        # 初始化结果字符串
        while len(res) < len(s):                        # 满足条件时执行
            res += s[left:mid][::-1] + s[mid:right]     # 把当前单元的结果添加到结果字符串
            left, mid, right = left + 2 * k, mid + 2 * k, right + 2 * k
        return res

test = Solution()
print(test.reverseStr("abcdefg", 2))
