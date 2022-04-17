from typing import List
class ATM:

    def __init__(self):
        self.notes = [0 for _ in range(5)]
        self.value = [20, 50, 100, 200, 500]
        self.sum = 0

    def deposit(self, banknotesCount: List[int]) -> None:
        for index, value in enumerate(banknotesCount):
            self.notes[index] += value
            self.sum += self.value[index] * value


    def withdraw(self, amount: int) -> List[int]:
        if amount % 10 != 0:
            return [-1]
        if amount > self.sum:
            return [-1]
        if amount == self.sum:
            self.notes = [0 for _ in range(5)]
            self.sum = 0
            return self.notes

        ans = [0 for _ in range(5)]
        
        for i in range(4, -1, -1):
            if amount >= self.value[i] and self.notes[i] > 0:
                draw = min(amount // self.value[i], self.notes[i])
                ans[i] = draw
                amount -= draw * self.value[i]

        if amount == 0:
            self.sum -= amount
            for i in range(5):
                self.notes[i] -= ans[i]
            return ans
        else:
            return [-1] 



# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)