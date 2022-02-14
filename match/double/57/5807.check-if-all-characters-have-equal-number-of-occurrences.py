class Solution:
    def are0ccurrencesEqual(self, s: str) -> bool:
        letter_count = list(set(list(s)))
        count = s.count(letter_count[0])
        for letter in letter_count:
            if s.count(letter) != count:
                return False
        return True