class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1count = {}

        for l in s1:
            s1count[l] = s1count.get(l, 0) + 1

        l = 0
        for r in range(len(s2)):
            s1count[s2[r]] = s1count.get(s2[r], 0) - 1
            while s1count[s2[r]] < 0:
                s1count[s2[l]] += 1
                l += 1
            if r - l + 1 == len(s1):
                return True
        return False