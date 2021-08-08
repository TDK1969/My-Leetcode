class Solution:
    def minSwaps(self, s: str) -> int:
        cnt, ans = 0, 0
        for char in s:
            if char == '[':
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:  # 如果出现cnt小于0，则表示出现了一个]应该被替换
                    cnt += 2  # 表示将当前的]换为[
                    ans += 1
        return ans