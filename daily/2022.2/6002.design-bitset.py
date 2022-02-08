class Bitset:

    def __init__(self, size: int):
        self.flag = True
        self.size = size
        self.sum = 0
        self.bitset = [0 for _ in range(size)]

    def fix(self, idx: int) -> None:
        if self.flag:
            if self.bitset[idx] == 0:
                self.bitset[idx] = 1
                self.sum += 1
        else:
            if self.bitset[idx] == 1:
                self.bitset[idx] = 0
                self.sum += 1


    def unfix(self, idx: int) -> None:
        if self.flag:
            if self.bitset[idx] == 1:
                self.bitset[idx] = 0
                self.sum -= 1
        else:
            if self.bitset[idx] == 0:
                self.bitset[idx] = 1
                self.sum -= 1


    def flip(self) -> None:
        self.flag = not self.flag
        self.sum = self.size - self.sum


    def all(self) -> bool:
        return self.sum == self.size


    def one(self) -> bool:
        return self.sum > 0


    def count(self) -> int:
        return self.sum


    def toString(self) -> str:
        ans = ''
        if self.flag:
            for bit in self.bitset:
                ans += (str(bit))
        else:
            for bit in self.bitset:
                if bit == 0:
                    ans += '1'
                if bit == 1:
                    ans += '0'

        return ans

test = Bitset(5)
test.fix(3)
test.fix(1)
test.flip()
print(test.all())
test.unfix(0)
test.flip()
print(test.one())
test.unfix(0)
print(test.count())
print(test.toString())