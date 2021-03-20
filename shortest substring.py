class Solution:    
    def combine(self, w1, w2):
        for i in range(len(w2), 0, -1):
            if w2[0 : i] == w1[len(w1) - i:]:
                return w1 + w2[i:]
        return w1 + w2
    
    def get(self,words, bitmask, prev, n, dp):
        if bitmask == 0:
            return prev
        if bitmask in dp and prev in dp[bitmask]:
            return dp[bitmask][prev]
        possible = []
        for i in range(n):
            if (bitmask & (1 << i)) == 0:
                continue
            new_bitmask = bitmask ^ (1 << i)
            possible.append(self.get(words, new_bitmask, self.combine(prev, words[i]), n, dp))
        
        possible.sort(key = len)
        dp[bitmask] = {prev: possible[0]}
        return possible[0]
        
        
    def shortestSuperstring(self, words: List[str]) -> str:
        dp = {}
        bitmask_limit = (1 << len(words)) - 1  #1111
        return self.get(words, bitmask_limit, "", len(words), dp)
