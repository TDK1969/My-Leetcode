from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        # 双指针-读写指针原地算法
        # 因为修改后的字符数组长度一定小于原数组，因此写指针一定不会超过读指针，即不会产生覆盖
        read = 0
        write = 0
        n = len(chars)
        while read < n:  # 读指针应该遍历整个字符数组
            count = 1
            nxt = read + 1
            while nxt < n and chars[nxt] == chars[read]:
                nxt += 1
                count += 1

            chars[write] = chars[read]
            write += 1
            if count > 1:
                for num in str(count):
                    chars[write] = num
                    write += 1
            read = nxt
        return write

test = Solution()
print(test.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))


