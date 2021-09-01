class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        temp1 = [int(s) for s in version1.split(".")]
        temp2 = [int(s) for s in version2.split(".")]
        if len(temp1) < len(temp2):
            for _ in range(len(temp2) - len(temp1)):
                temp1.append(0)
        if len(temp1) > len(temp2):
            for _ in range(len(temp1) - len(temp2)):
                temp2.append(0)
        if temp1 > temp2:
            return 1
        elif temp1 < temp2:
            return -1
        else:
            return 0

test = Solution()
print(test.compareVersion(version1 = "1.0", version2 = "1.0.0"))