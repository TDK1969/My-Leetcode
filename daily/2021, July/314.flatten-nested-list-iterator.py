class NestedIterator:

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList
        self.stack = [[self.nestedList, 0]]
        self.ans = []
        while self.stack:
            temp, top = self.stack[-1]
            next_elem = temp[top]
            top += 1
            self.stack[-1][1] += 1
            if top == len(temp):
                self.stack.pop()
            if isinstance(next_elem, list):
                self.stack.append([next_elem, 0])
            elif isinstance(next_elem, int):
                self.ans.append(next_elem)

    def next(self):
        """
        :rtype: int
        """
        return self.ans.pop(0)


    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.ans)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

test = NestedIterator([[1,1],2,[1,1]])
v = []
while test.hasNext():
    v.append(test.next())
print(v)
