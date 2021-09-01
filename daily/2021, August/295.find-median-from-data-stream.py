import bisect
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.steam = []


    def addNum(self, num: int) -> None:
        bisect.bisect(self.steam, num)
        self.steam.insert(bisect.bisect(self.steam, num), num)

    def findMedian(self) -> float:
        n = len(self.steam)
        if n & 1:
            return float(self.steam[n // 2])
        else:
            return (self.steam[n // 2] + self.steam[(n // 2) - 1]) / 2




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()