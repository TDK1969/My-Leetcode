from sortedcontainers import SortedList
class StockPrice:

    def __init__(self):
        self.SortedList = SortedList()
        self.tp = {}
        self.curTime = 0


    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.tp:
            self.SortedList.remove(self.tp[timestamp])
        self.SortedList.add(price)
        self.tp[timestamp] = price
        self.curTime = max(self.curTime, timestamp)

    def current(self) -> int:
        return self.tp[self.curTime]

    def maximum(self) -> int:
        return self.SortedList[-1]


    def minimum(self) -> int:
        return self.SortedList[0]
