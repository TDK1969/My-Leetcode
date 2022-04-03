from typing import List
from collections import defaultdict

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.kv = {}
        self.count = 0
        self.vk = defaultdict(list)
        self.answer = dict()
        for key, value in zip(keys, values):
            self.kv[key] = value
            self.vk[value].append(key)
        
        maxLen = max([len(i) for i in dictionary])
        self.dictionary = [set() for _ in range(maxLen)]
        self.dictLen = set([len(i) for i in dictionary])

        for j in range(maxLen):
            self.dictionary[j] = set([i[:j + 1] for i in dictionary])

    def encrypt(self, word1: str) -> str:
        ans = ""
        for char in word1:
            ans += self.kv[char]
        return ans

    def decrypt(self, word2: str) -> int:
        self.count = 0
        if word2 in self.answer:
            return self.answer[word2]
        elif len(word2) // 2 in self.dictLen:
            self.dfs(word2, "", 0)
            self.answer[word2] = self.count
        return self.count

    def dfs(self, word2: str, temp: str, index: int):
        if index == len(word2) and temp in self.dictionary[-1]:
            self.count += 1
        elif index < len(word2):
            curValue = word2[index : index + 2]
            for key in self.vk[curValue]:
                temp1 = temp + key
                if temp1 in self.dictionary[index // 2]:
                    self.dfs(word2, temp1, index + 2)



test = Encrypter(['a', 'b', 'c', 'z'], ["aa", "bb", "cc", "zz"], ["aa", "aaa", "aaaa", "aaaaa", "aaaaaaa"])
#print(test.encrypt("abcd"))
print(test.decrypt("aa"))