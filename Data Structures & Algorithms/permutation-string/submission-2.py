class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        l = 0

        for letter in s1:
            count[letter] = count.get(letter, 0) + 1

        for r in range(len(s2)):
            count[s2[r]] = count.get(s2[r], 0) - 1
            while count[s2[r]] < 0:
                count[s2[l]] += 1
                l += 1
            if r - l + 1 == len(s1):
                return True
        return False