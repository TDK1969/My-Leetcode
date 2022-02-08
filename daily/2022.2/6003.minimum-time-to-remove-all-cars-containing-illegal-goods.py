from collections import deque
class Solution:
    def minimumTime(self, s: str) -> int:
        if not s:
            return 0

        sum = s.count('1')
        train = deque(list(s))
        cost = 0

        ones = deque()
        for i, value in enumerate(train):
            if value == '1':
                ones.append(i)


        while sum:
            while train and train[0] == '1':
                train.popleft()
                ones.popleft()
                cost += 1
                sum -= 1
            while train and train[-1] == '1':
                train.pop()
                ones.pop()
                cost += 1
                sum -= 1
            while len(train) > 2 and train[0] == '0' and train[1] == '1':
                train.popleft()
                train.popleft()
                ones.popleft()
                cost += 2
                sum -= 1
            while len(train) > 2 and train[-1] == '0' and train[-2] == '1':
                train.pop()
                train.pop()
                ones.pop()
                cost += 2
                sum -= 1





