class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_t, count_s = {}, {} # letter: number of occurances
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        return count_s == count_t

        