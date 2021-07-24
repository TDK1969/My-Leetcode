class Solution:
    def maximumTime(self, time: str) -> str:
        t = list(time)
        ans = ""

        if t[0] == t[1] == '?':
            t[0] = '2'
            t[1] = '3'
        elif t[0] == '?':
            if int(t[1]) > 3:
                t[0] = '1'
            else:
                t[0] = '2'
        elif t[1] == '?':
            if int(t[0]) == 2:
                t[1] = '3'
            else:
                t[1] = '9'

        if t[3] == '?':
            t[3] = '5'
        if t[4] == '?':
            t[4] = '9'

        return ''.join(t)

test = Solution()
print(test.maximumTime("2?:?0"))