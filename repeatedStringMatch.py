class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        ceil = -(-len(b) // len(a)) # ciel of len(b) / len(a)
        if b in a * ceil:
            return ceil
        if b in a * (ceil + 1):
            return ceil + 1
        return -1
